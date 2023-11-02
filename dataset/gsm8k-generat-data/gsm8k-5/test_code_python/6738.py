def solution():
    primary_tank_time = 2  # The primary tank allows Beth to stay underwater for 2 hours
    total_time = 8  # Beth needs to be underwater for 8 hours
    supplemental_tank_time = 1  # Each supplemental tank allows Beth to stay underwater for 1 hour

    # Calculate the total time Beth can stay underwater using only the primary tank
    remaining_time = total_time - primary_tank_time

    # Calculate the number of supplemental tanks Beth needs
    num_supplemental_tanks = remaining_time // supplemental_tank_time

    result = num_supplemental_tanks
    return result

print(solution())