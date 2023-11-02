def solution():
    """A cobbler can mend 3 pairs of shoes in an hour. From Monday to Thursday, the cobbler works for 8 hours each day, and on Friday, he only works from 8am to 11am. How many pairs of shoes can the cobbler mend in a week?"""
    # Define the number of hours worked each day
    HOURS_MON_THU = 8
    HOURS_FRI = 3

    # Define the number of pairs of shoes mended per hour
    SHOES_PER_HOUR = 3

    # Calculate the total number of hours worked in the week
    total_hours = (HOURS_MON_THU * 4) + HOURS_FRI

    # Calculate the total number of pairs of shoes mended in the week
    total_shoes = SHOES_PER_HOUR * total_hours

    # Display the total number of pairs of shoes mended in the week
    result = total_shoes
    return result

print(solution())