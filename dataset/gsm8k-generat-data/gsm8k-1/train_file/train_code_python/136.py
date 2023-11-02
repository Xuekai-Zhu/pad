def solution():
    """3 families of 4 people shared a vacation rental for 7 days. Everyone uses 1 oversized beach towel a day before getting a new one. The washing machine can hold 14 oversized beach towels per load. How many loads of laundry will it take to wash all the oversized beach towels?"""
    families = 3
    people_per_family = 4
    days = 7
    towels_per_person_per_day = 1
    total_towels = families * people_per_family * days * towels_per_person_per_day
    towels_per_load = 14
    total_loads = int(total_towels / towels_per_load + 1)
    result = total_loads
    return result

print(solution())