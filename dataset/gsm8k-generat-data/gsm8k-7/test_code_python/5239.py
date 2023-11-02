def solution():
    num_bags = 4
    peanuts_per_bag = 30
    total_peanuts = num_bags * peanuts_per_bag
    flight_time_hours = 2
    flight_time_minutes = flight_time_hours * 60
    time_between_peanuts = flight_time_minutes / (total_peanuts - 1)
    result = time_between_peanuts
    return result

print(solution())