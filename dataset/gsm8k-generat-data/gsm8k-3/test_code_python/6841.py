def solution():
    """Janet takes two multivitamins and 3 calcium supplements every day for the first 2 weeks of the month. For the last two weeks of the month, she runs low on calcium supplements and only takes one per day. How many pills does Janet take in that month?"""
    # Calculate the number of days in the first two weeks of the month
    days_in_first_two_weeks = 14

    # Calculate the number of pills Janet takes in the first two weeks
    pills_in_first_two_weeks = (2 * 2 + 3 * 3) * days_in_first_two_weeks

    # Calculate the number of days in the last two weeks of the month
    days_in_last_two_weeks = 14

    # Calculate the number of pills Janet takes in the last two weeks
    pills_in_last_two_weeks = (2 * 2 + 1 * 3) * days_in_last_two_weeks

    # Calculate the total number of pills Janet takes in the month
    total_pills = pills_in_first_two_weeks + pills_in_last_two_weeks

    # Display the total number of pills Janet takes in the month
    result = total_pills
    return result

print(solution())