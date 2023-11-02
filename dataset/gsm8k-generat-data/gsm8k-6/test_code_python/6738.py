def solution():
    # Calculate the number of supplemental tanks Beth will need
    hours_needed = 8  # Beth needs to be underwater for 8 hours
    primary_tank = 2  # Beth's primary tank lasts for 2 hours
    supplemental_tank = 1  # Each supplemental tank lasts for 1 hour
    total_tank_hours = primary_tank + (supplemental_tank * x)  # Calculate the total number of hours that the tanks can provide
    while total_tank_hours < hours_needed:  # Keep adding supplemental tanks until the total hours are sufficient
        x += 1
        total_tank_hours = primary_tank + (supplemental_tank * x)
    result = x
    return result

print(solution())