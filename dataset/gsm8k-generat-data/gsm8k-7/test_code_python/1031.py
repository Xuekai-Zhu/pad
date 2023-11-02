def solution():
    num_people_start = 600
    num_girls_start = 240

    # Calculate the number of boys at the beginning of the game
    num_boys_start = num_people_start - num_girls_start

    # Calculate the number of boys who left early
    num_boys_left = num_boys_start / 4

    # Calculate the number of girls who left early
    num_girls_left = num_girls_start / 8

    # Calculate the total number of people who left early
    num_people_left = num_boys_left + num_girls_left

    # Calculate the total number of people who remained to see the end of the game
    num_people_end = num_people_start - num_people_left
    result = num_people_end
    return result

print(solution())