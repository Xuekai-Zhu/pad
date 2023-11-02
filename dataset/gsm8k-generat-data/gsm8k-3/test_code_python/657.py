def solution():
    """Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)"""
    # Define the total travel time in minutes
    total_travel_time = 90  # 10 minutes walk + 80 minutes train ride

    # Define the desired arrival time as a string in 24-hr time format
    desired_arrival_time = '09:00'

    # Convert the desired arrival time to minutes since midnight
    desired_arrival_minutes = int(desired_arrival_time[:2]) * 60 + int(desired_arrival_time[3:])

    # Subtract the total travel time from the desired arrival time to get the latest departure time
    latest_departure_minutes = desired_arrival_minutes - total_travel_time

    # Convert the latest departure time to a string in 24-hr time format
    latest_departure_time = f"{latest_departure_minutes//60:02}:{latest_departure_minutes%60:02}"

    # Display the latest departure time
    result = latest_departure_time
    return result

print(solution())