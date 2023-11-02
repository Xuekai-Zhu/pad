def solution():
    """A cobbler can mend 3 pairs of shoes in an hour. From Monday to Thursday, the cobbler works for 8 hours each day, and on Friday, he only works from 8am to 11am. How many pairs of shoes can the cobbler mend in a week?"""
    # Define the number of hours worked each day
    hours_per_day = 8

    # Define the number of hours worked on Friday
    friday_hours = 3

    # Calculate the total number of pairs of shoes mended from Monday to Thursday
    mended_shoes_mon_thu = 3 * hours_per_day * 4

    # Calculate the total number of pairs of shoes mended on Friday
    mended_shoes_fri = 3 * friday_hours

    # Calculate the total number of pairs of shoes mended in a week
    mended_shoes_total = mended_shoes_mon_thu + mended_shoes_fri

    result = mended_shoes_total
    return result

print(solution())