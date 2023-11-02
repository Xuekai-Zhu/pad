def solution():
    # Calculate the total number of minutes tanned in the first two weeks
    first_two_weeks = 30 * 2 * 2

    # Calculate the maximum number of minutes Jenna can tan in the last two weeks
    max_last_two_weeks = 200 - first_two_weeks

    # Return the maximum number of minutes Jenna can tan in the last two weeks
    return max_last_two_weeks

print(solution())