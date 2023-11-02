def solution():
    """Amber and Josh are flying to France for vacation. Their flight leaves at 8:00 pm and as an international flight, it's recommended that they check in 2 hours early. It will take 45 minutes to drive to the airport and another 15 minutes to park their vehicle and make their way to the terminal. What is the latest time they can leave their house to make it to the airport in time?"""
    flight_time = 20  # 8:00 pm
    check_in_time = 2  # hours
    drive_time = 0.75  # 45 minutes
    terminal_time = 0.25  # 15 minutes
    total_time = check_in_time + drive_time + terminal_time  # hours
    latest_departure_time = flight_time - total_time  # hours
    result = latest_departure_time
    return result

print(solution())