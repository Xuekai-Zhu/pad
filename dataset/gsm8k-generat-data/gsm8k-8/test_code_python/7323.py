def solution():
    # Define the recommended check-in time and total travel time to the airport
    recommended_check_in = 2
    travel_time = 0.75  # 45 minutes to drive and 15 minutes to park and reach the terminal

    # Calculate the latest time they can leave their house
    latest_time = datetime.time(hour=20) - datetime.timedelta(hours=recommended_check_in+travel_time)

    result = latest_time
    return result

print(solution())