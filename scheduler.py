# scheduler.py
import schedule
import time
from main import run_daily_agent

def start_scheduler():
    """
    Schedule the AI agent to run daily at 9 AM IST.
    """
    schedule.every().day.at("09:00").do(run_daily_agent)
    print("Scheduler started... Running daily at 09:00 IST")
    while True:
        schedule.run_pending()
        time.sleep(60)

# Test
if __name__ == "__main__":
    start_scheduler()
