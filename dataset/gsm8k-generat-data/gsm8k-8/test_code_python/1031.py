def solution():
    # Calculate the initial number of boys
    initial_boys = 600 - 240

    # Calculate the number of boys who left early
    boys_left_early = initial_boys / 4

    # Calculate the number of girls who left early
    girls_left_early = 240 / 8

    # Calculate the total number of people who left early
    total_left_early = boys_left_early + girls_left_early

    # Calculate the number of people who remained to see the end of the game
    remained = 600 - total_left_early
    result = remained
    return result

print(solution())