# Import Library
import datetime

# Get time for start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = int(start_time[0])
start_minute = int(start_time[1])
start_second = float(start_time[2])


# Get time for stop
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = int(stop_time[0])
stop_minute = int(stop_time[1])
stop_second = float(stop_time[2])

difference = float(stop_second) - float(start_second)
print(difference)

difference = int(stop_minute) - int(start_minute)
print(difference)

difference = int(stop_hour) - int(start_hour)
print(difference)

# Adjust if the seconds or minutes go negative
if stop_second < 0:
    stop_second += 60
    stop_minute -= 1

