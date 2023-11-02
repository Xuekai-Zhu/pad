def solution():
    # Define the number of pills Janet takes in the first two weeks
    pills_first_two_weeks = (2*14) + (3*14)

    # Define the number of pills Janet takes in the last two weeks
    pills_last_two_weeks = (2*7) + (1*7)

    # Calculate the total number of pills Janet takes in the month
    total_pills = pills_first_two_weeks + pills_last_two_weeks
    result = total_pills
    return result

print(solution())