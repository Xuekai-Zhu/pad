def solution():
    capacity_per_20_min = 70
    num_hours = 6  # from 1:00 pm to 7:00 pm

    # Calculate the total number of 20-minute intervals during the operating hours
    total_intervals = num_hours * 3  # 3 intervals per hour

    # Calculate the total capacity of the Ferris wheel during operating hours
    total_capacity = total_intervals * capacity_per_20_min

    result = total_capacity
    return result

print(solution())