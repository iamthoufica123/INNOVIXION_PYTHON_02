import datetime
import time
import os

def set_alarm():
    print("Enter the time for the alarm (format: HH:MM):")
    alarm_time = input("> ")

    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60:
            return datetime.time(alarm_hour, alarm_minute)
        else:
            print("Invalid time! Please enter a valid time.")
            return set_alarm()
    except ValueError:
        print("Invalid time! Please enter a valid time.")
        return set_alarm()

def main():
    print("Welcome to the Python Alarm Clock App!")
    alarm_time = set_alarm()

    print(f"Alarm set for {alarm_time.strftime('%H:%M')}.")

    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("Wake up! Alarm ringing!")
            # You can add any notification mechanism here, like playing a sound.
            break
        else:
            # Check every second
            time.sleep(1)

if __name__ == "__main__":
    main()
