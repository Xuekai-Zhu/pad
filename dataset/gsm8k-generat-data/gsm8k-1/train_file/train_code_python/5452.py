def solution():
    """It takes Bryan 5 minutes to walk from his house to the bus station. Then he rides the bus for 20 minutes. After that, he walks 5 minutes from the bus station to his job. It takes the same amount of time in the morning and the evening. How many hours per year does Bryan spend traveling to and from work, if he works every day?"""
    time_to_bus = 5
    bus_ride = 20
    time_to_work = 5
    total_time_per_trip = time_to_bus + bus_ride + time_to_work
    total_time_per_day = total_time_per_trip * 2
    total_time_per_year = total_time_per_day * 365
    hours_per_year = total_time_per_year / 60
    result = hours_per_year
    return result

print(solution())