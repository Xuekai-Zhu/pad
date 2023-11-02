def solution():
    # Calculate the total tanning time in the first two weeks of the month
    tanning_time_first_two_weeks = 30 * 2 * 2

    # Calculate the remaining tanning time she can have in the last two weeks of the month
    remaining_tanning_time = 200 - tanning_time_first_two_weeks

    result = remaining_tanning_time
    return result

print(solution())