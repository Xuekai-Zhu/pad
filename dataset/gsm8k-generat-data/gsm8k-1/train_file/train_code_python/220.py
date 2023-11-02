def solution():
    """Mira jogs every morning. She jogs 5 miles per hour. If she jogs for 2 hours every morning, how many miles can she jog for five days?"""
    speed = 5 # miles per hour
    time_jogging = 2 # hours per day
    days_jogging = 5
    miles_jogged = speed * time_jogging
    total_miles_jogged = miles_jogged * days_jogging
    result = total_miles_jogged
    return result

print(solution())