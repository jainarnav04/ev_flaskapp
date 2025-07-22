# scheduler.py
from auth import app, update_all_station_wait_times, remove_completed_vehicles
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

def start_scheduler():
    print("Starting scheduler...")
    scheduler = BlockingScheduler()
    scheduler.add_job(update_all_station_wait_times, 'interval', minutes=1)
    scheduler.add_job(remove_completed_vehicles, 'interval', minutes=1)
    scheduler.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with app.app_context():
        start_scheduler()