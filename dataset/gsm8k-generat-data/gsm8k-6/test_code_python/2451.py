def solution():
    # Calculate the number of towels Sanya can wash in 2 hours
    total_wash_time = 2  # total time available in a day
    towels_per_wash = 7  # number of towels per wash
    washes_in_2_hours = total_wash_time * 60 // 1 * (1/60) // 1 // 1 * towels_per_wash  # convert to minutes and round down, then to hours and round down, then to number of washes

    # Calculate the number of days needed to wash all towels
    total_towels = 98  # total number of towels
    days_to_wash_all_towels = total_towels // washes_in_2_hours + (total_towels % washes_in_2_hours > 0)  # divide and round up to get the number of days needed

    result = days_to_wash_all_towels
    return result

print(solution())