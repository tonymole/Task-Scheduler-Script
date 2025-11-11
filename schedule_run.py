#  pip install schedule

import schedule
import time
import datetime


def greet_user():
    """A function to print a greeting."""
    print("Hello! This is a scheduled greeting.")


def log_time():
    """A function to log the current time."""
    now = datetime.datetime.now()
    print(f"Current time logged: {now}")


def daily_report():
    """A function to simulate generating a daily report."""
    print("Generating daily report...")
    # In a real application, this would involve more complex logic
    # like data retrieval, processing, and output.


# Schedule tasks
schedule.every(10).seconds.do(greet_user)  # Run greet_user every 10 seconds
schedule.every(1).minute.do(log_time)  # Run log_time every minute
schedule.every().day.at("08:00").do(daily_report)  # Run daily_report every day at 8 AM

print("Scheduler started. Press Ctrl+C to stop.")

# Main loop to run pending scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
