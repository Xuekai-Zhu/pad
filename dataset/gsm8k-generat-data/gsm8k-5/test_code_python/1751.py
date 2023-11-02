def solution():
    sewer_capacity = 240000  # Sewers in Middleton can handle 240,000 gallons of run-off
    rain_per_hour = 1000  # Each hour of rain produces 1000 gallons of runoff
    hours_until_overflow = sewer_capacity / rain_per_hour  # Calculate how many hours it takes before the sewers overflow
    days_until_overflow = hours_until_overflow / 24  # Convert hours until overflow to days until overflow
    result = days_until_overflow
    return result

print(solution())