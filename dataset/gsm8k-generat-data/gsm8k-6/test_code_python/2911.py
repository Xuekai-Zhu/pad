def solution():
    # Calculate the number of granola bars that Greg saved for the week
    saved_bars = 7  # one for each day of the week

    # Calculate the number of granola bars left after trading with his friend
    remaining_bars = 20 - saved_bars - 3

    # Calculate the number of granola bars each sister gets when they split them evenly
    each_sister_gets = remaining_bars // 2

    result = each_sister_gets
    return result

print(solution())