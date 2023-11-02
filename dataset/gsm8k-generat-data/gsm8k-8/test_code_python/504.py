def solution():
    # Calculate Sam's hourly rate for yard work in March-August
    rate_1 = 460 / 23

    # Calculate how much Sam earned from September-February
    earned_2 = rate_1 * 8

    # Calculate how much Sam has saved so far
    saved = earned_2 + 460 - 340

    # Calculate how much Sam still needs to save
    remaining = 600 - saved

    # Calculate how many more hours Sam needs to work to reach his goal
    hours_needed = remaining / rate_1
    result = hours_needed
    return result

print(solution())