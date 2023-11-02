def solution():
    # Calculate the total number of extra chores Edmund needs to do
    extra_chores_needed = 75 / 2

    # Calculate the total number of chores Edmund needs to do
    total_chores_needed = 12 * 2 * 7

    # Calculate the number of extra chores Edmund needs to do each day
    extra_chores_per_day = extra_chores_needed / 14

    # Calculate the total number of extra chores Edmund does over two weeks
    total_extra_chores = extra_chores_per_day * 4 * 14

    # Calculate Edmund's total earnings
    total_earnings = total_extra_chores * 2

    result = total_earnings
    return result

print(solution())