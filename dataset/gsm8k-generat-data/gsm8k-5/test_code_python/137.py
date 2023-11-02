def solution():
    num_people = 3 * 4  # There are a total of 12 people sharing the rental
    towels_per_day = num_people  # Each person uses one towel per day
    total_towels = towels_per_day * 7  # There are 7 days in the rental period

    # Calculate the number of loads of laundry required to wash all the towels
    loads_required = total_towels // 14
    if total_towels % 14 != 0:  # If there are any towels leftover, add another load
        loads_required += 1
    result = loads_required
    return result

print(solution())