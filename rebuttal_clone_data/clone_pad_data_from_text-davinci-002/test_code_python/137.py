def solution():
     """3 families of 4 people shared a vacation rental for 7 days. Everyone uses 1 oversized beach towel a day before getting a new one. The washing machine can hold 14 oversized beach towels per load. How many loads of laundry will it take to wash all the oversized beach towels?"""
     families = 3
     people_per_family = 4
     days_of_use = 7
     towels_used = families * people_per_family * days_of_use
     towels_per_load = 14
     loads_of_laundry = towels_used / towels_per_load
     result = loads_of_laundry
     return result

print(solution())