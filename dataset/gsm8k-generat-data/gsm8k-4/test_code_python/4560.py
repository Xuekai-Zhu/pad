def solution():
    """James writes a comic every other day for 4 years. If there was no leap year, how many comics has he written?"""
    # Define the number of days in 4 years
    num_days = 365 * 4

    # Calculate the number of comics he writes each day
    num_comics_per_day = 1 / 2

    # Calculate the total number of comics he writes in 4 years
    num_comics = num_comics_per_day * num_days

    # Round the result to the nearest whole number
    result = round(num_comics)

    return result

print(solution())