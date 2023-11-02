def solution():
    """Jenna's doctor tells her that she should tan no more than 200 minutes a month. If she tans 30 minutes a day, two days a week for the first two weeks of the month, how many minutes can she tan in the last two weeks of the month?"""
    # Calculate the total minutes Jenna tans in the first two weeks
    tanning_minutes = 30 * 2 * 2

    # Calculate the minutes Jenna can tan in the last two weeks
    remaining_minutes = 200 - tanning_minutes

    # Display the remaining minutes Jenna can tan
    result = remaining_minutes
    return result

print(solution())