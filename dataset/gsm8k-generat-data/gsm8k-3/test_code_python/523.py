def solution():
    """Hayes does 3 loads of laundry a week using a detergent pod for each load.  His detergent pods come 39 to a pack.  How many packs of detergent pods will he need to do a full year of laundry?"""
    # Define the number of loads of laundry Hayes does per week and per year
    loads_per_week = 3
    weeks_per_year = 52
    loads_per_year = loads_per_week * weeks_per_year

    # Define the number of detergent pods per pack
    pods_per_pack = 39

    # Calculate the number of packs of detergent pods needed for a full year of laundry
    packs_needed = loads_per_year / pods_per_pack
    packs_needed = round(packs_needed) # Round up to the nearest pack

    # Display the number of packs of detergent pods needed
    result = packs_needed
    return result

print(solution())