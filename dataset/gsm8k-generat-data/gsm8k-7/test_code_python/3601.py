def solution():
    first_two_tanks = 8
    second_two_tanks = first_two_tanks - 2
    num_tanks = 4
    num_weeks = 4

    # Calculate the total amount of water needed for the first two tanks
    water_needed_first_two = first_two_tanks * 2

    # Calculate the total amount of water needed for the second two tanks
    water_needed_second_two = second_two_tanks * 2

    # Calculate the total amount of water needed for all tanks
    total_water_needed = water_needed_first_two + water_needed_second_two

    # Calculate the total amount of water needed for all weeks
    total_water_needed_all_weeks = total_water_needed * num_weeks

    result = total_water_needed_all_weeks
    return result

print(solution())