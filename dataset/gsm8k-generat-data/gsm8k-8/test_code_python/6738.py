def solution():
    # Calculate the total time she needs to be underwater
    total_time = 8

    # Calculate the time her primary tank will last
    primary_tank_time = 2

    # Calculate the remaining time she needs
    remaining_time = total_time - primary_tank_time

    # Calculate the number of supplemental tanks needed
    num_supplemental_tanks = remaining_time / 1

    result = num_supplemental_tanks
    return result

print(solution())