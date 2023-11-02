def solution():
    """Jenna's doctor tells her that she should tan no more than 200 minutes a month. If she tans 30 minutes a day, two days a week for the first two weeks of the month, how many minutes can she tan in the last two weeks of the month?"""
    # Define the maximum number of minutes Jenna can tan in a month
    MAX_MINUTES = 200

    # Calculate the total number of minutes Jenna has already tanned in the first two weeks
    tanned_minutes = 30 * 2 * 2

    # Calculate the remaining number of minutes Jenna can tan in the last two weeks
    remaining_minutes = MAX_MINUTES - tanned_minutes

    # return the result
    result = remaining_minutes
    return result

print(solution())