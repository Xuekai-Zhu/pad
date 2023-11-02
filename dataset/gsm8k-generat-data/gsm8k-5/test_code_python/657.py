def solution():
    # Convert the train time to minutes
    train_time = 80  # 1 hour 20 minutes
    train_time_minutes = train_time * 60

    # Calculate the latest time Pete can leave to get to LA by 9:00 AM
    latest_arrival_time = 9 * 60

    # Subtract the train time and the 10-minute walk from the latest arrival time to get the latest departure time
    latest_departure_time = latest_arrival_time - train_time_minutes - 10

    # Convert the latest departure time to 24-hour format
    hours = latest_departure_time // 60
    minutes = latest_departure_time % 60

    # Format the result as a string in 24-hour format
    result = "{:02d}:{:02d}".format(hours, minutes)
    return result

print(solution())