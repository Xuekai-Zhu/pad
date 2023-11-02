def solution():
    """3 families of 4 people shared a vacation rental for 7 days. 
    Everyone uses 1 oversized beach towel a day before getting a new one. 
    The washing machine can hold 14 oversized beach towels per load. 
    How many loads of laundry will it take to wash all the oversized beach towels?"""
    
    # Define the number of families and the number of days of the vacation
    num_families = 3
    num_people_per_family = 4
    num_days = 7
    
    # Calculate the total number of beach towels used
    num_towels_used = num_families * num_people_per_family * num_days
    
    # Calculate the number of loads of laundry needed
    num_loads = num_towels_used // 14
    if num_towels_used % 14 != 0:
        num_loads += 1
        
    result = num_loads
    return result

print(solution())