# scheduler.py
import logging
from datetime import datetime
from auth import app, update_all_station_wait_times, remove_completed_vehicles  # Fixed import

def run_scheduled_tasks():
    """Run tasks once and exit - perfect for cron jobs"""
    print(f"🚀 Starting scheduled tasks at: {datetime.now()}")
    
    try:
        with app.app_context():
            print("📊 Updating station wait times...")
            update_all_station_wait_times()
            print("✅ Station wait times updated successfully")
            
            print("🚗 Removing completed vehicles...")
            remove_completed_vehicles()
            print("✅ Completed vehicles removed successfully")
            
            print("🎉 All scheduled tasks completed!")
            
    except Exception as e:
        print(f"❌ Error in scheduled tasks: {e}")
        logging.error(f"Scheduler error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    run_scheduled_tasks()
    print("👋 Scheduler script exiting...")
