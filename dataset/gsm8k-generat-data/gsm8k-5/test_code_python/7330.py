def solution():
    sand_dug_up = 8  # Pirate Rick dug up 8 feet of sand to bury his treasure
    sand_left_after_storm = sand_dug_up / 2  # The storm washed away half of the sand
    sand_after_tsunami = sand_left_after_storm + 2  # The tsunami added 2 feet of sand back

    # Calculate the total amount of sand that needs to be dug up again
    sand_to_dig_up = sand_dug_up - sand_left_after_storm

    # Calculate the time it will take to dig up the treasure again
    time_to_dig_up = sand_to_dig_up / sand_dug_up * 4  # 4 hours to dig up 8 feet of sand
    result = time_to_dig_up
    return result

print(solution())