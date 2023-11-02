def solution():
    # Calculate the number of boys at the beginning of the game
    boys_start = 600 - 240  # if there were 240 girls, then there were 360 boys

    # Calculate the number of boys and girls who left early
    boys_left = boys_start / 4
    girls_left = 240 / 8

    # Calculate the total number of people who left early
    people_left = boys_left + girls_left

    # Calculate the number of people who remained to see the end of the game
    people_remain = 600 - people_left

    result = people_remain
    return result

print(solution())