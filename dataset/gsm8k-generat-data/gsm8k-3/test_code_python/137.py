def solution():
    """3 families of 4 people shared a vacation rental for 7 days. Everyone uses 1 oversized beach towel a day before getting a new one. The washing machine can hold 14 oversized beach towels per load. How many loads of laundry will it take to wash all the oversized beach towels?"""
    # Define the number of families and people per family
    num_families = 3
    num_people = 4

    # Calculate the total number of oversized beach towels used
    towels_used = num_families * num_people * 7

    # Calculate the number of loads of laundry needed to wash all the towels
    laundry_load_size = 14
    laundry_loads = towels_used // laundry_load_size + 1

    # Return the result
    result = laundry_loads
    return result

print(solution())