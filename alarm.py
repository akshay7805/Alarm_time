import time 
from datetime import datetime
def set_alarm(alarm_time):
    try:

        alarm_time=datetime.strptime(alarm_time,"%H:%M:%S").time()
        print(f"Alarm set for {alarm_time}")

        while True:
            current_time=datetime.now().time()
            if current_time>=alarm_time:
                print("Alarm is ringing Please wake up!")
                break
            time.sleep(1)
    except ValueError:
        print("Invalid format please enter valid format")
set_alarm("15:17:00")                
          
