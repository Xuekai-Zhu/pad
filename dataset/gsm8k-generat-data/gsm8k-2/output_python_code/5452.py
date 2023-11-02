def solution():
    """It takes Bryan 5 minutes to walk from his house to the bus station. Then he rides the bus for 20 minutes. After that, he walks 5 minutes from the bus station to his job. It takes the same amount of time in the morning and the evening. How many hours per year does Bryan spend traveling to and from work, if he works every day?"""
    total_travel_time = (5 + 20 + 5) * 2 # double for morning and evening
    minutes_per_year = 365 * 60 * 24 # minutes in a year
    total_hours_per_year = total_travel_time * minutes_per_year / 60
    result = total_hours_per_year
    return result

print(solution())