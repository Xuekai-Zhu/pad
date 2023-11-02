def solution():
    """Janet takes two multivitamins and 3 calcium supplements every day for the first 2 weeks of the month. For the last two weeks of the month, she runs low on calcium supplements and only takes one per day. How many pills does Janet take in that month?"""
    # Define the number of days in a month
    DAYS_IN_MONTH = 30

    # Calculate the number of pills Janet takes in the first two weeks
    pills_2_weeks = (2 * 14) + (3 * 14)

    # Calculate the number of pills Janet takes in the last two weeks
    pills_last_2_weeks = (2 * 7) + (1 * 14)

    # Calculate the total number of pills Janet takes in the entire month
    total_pills = pills_2_weeks + pills_last_2_weeks

    # return the result
    result = total_pills
    return result

print(solution())