def solution():
    # Define the water needed for each tank
    tank1_water = 8
    tank2_water = 8
    tank3_water = tank1_water - 2
    tank4_water = tank2_water - 2

    # Calculate the total water needed for one week
    weekly_water = tank1_water + tank2_water + tank3_water + tank4_water

    # Calculate the total water needed for four weeks
    four_weeks_water = weekly_water * 4
    result = four_weeks_water
    return result

print(solution())