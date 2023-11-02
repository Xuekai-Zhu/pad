def solution():
    # Calculate the total time Pete will spend traveling
    total_time = 10 + 80  # 10 minutes to walk to station and 1 hour 20 minutes on the train

    # Calculate the latest time Pete can leave to arrive in LA by 9:00 am
    latest_departure_time = 900 - total_time  # 900 is the time Pete needs to arrive by, in 24-hour format

    # Convert latest_departure_time to a formatted string in hh:mm format
    hours = latest_departure_time // 60
    minutes = latest_departure_time % 60
    latest_departure_str = "{:02d}:{:02d}".format(hours, minutes)
    result = latest_departure_str
    return result

print(solution())