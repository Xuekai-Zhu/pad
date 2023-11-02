def solution():
    """Jenna's doctor tells her that she should tan no more than 200 minutes a month. If she tans 30 minutes a day, two days a week for the first two weeks of the month, how many minutes can she tan in the last two weeks of the month?"""
    max_tanning_minutes = 200
    first_half_tanning_minutes = 2 * 2 * 30 * 2
    remaining_tanning_minutes = max_tanning_minutes - first_half_tanning_minutes
    result = remaining_tanning_minutes
    return result

print(solution())