def solution():
    """3 families of 4 people shared a vacation rental for 7 days. Everyone uses 1 oversized beach towel a day before getting a new one. The washing machine can hold 14 oversized beach towels per load. How many loads of laundry will it take to wash all the oversized beach towels?"""
    num_families = 3
    num_people_per_family = 4
    num_days = 7
    num_towels_per_day = num_families * num_people_per_family
    num_towels_total = num_towels_per_day * num_days
    towels_per_load = 14
    num_loads = num_towels_total // towels_per_load + (1 if num_towels_total % towels_per_load != 0 else 0 )
    result = num_loads
    return result

print(solution())