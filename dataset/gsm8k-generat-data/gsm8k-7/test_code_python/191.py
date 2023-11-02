def solution():
    initial_weasels = 100
    initial_rabbits = 50
    num_foxes = 3
    weasels_caught_weekly = 4
    rabbits_caught_weekly = 2
    num_weeks = 3

    # Calculate the total number of weasels caught by the foxes over 3 weeks
    total_weasels_caught = num_foxes * weasels_caught_weekly * num_weeks

    # Calculate the total number of rabbits caught by the foxes over 3 weeks
    total_rabbits_caught = num_foxes * rabbits_caught_weekly * num_weeks

    # Calculate the number of weasels and rabbits left after the foxes hunt
    num_weasels_left = initial_weasels - total_weasels_caught
    num_rabbits_left = initial_rabbits - total_rabbits_caught

    result = (num_weasels_left, num_rabbits_left)
    return result

print(solution())