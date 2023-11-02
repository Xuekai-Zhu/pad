def solution():
    """Barney washes his kitchen towels once a week. He owns eighteen towels and uses two at a time that he changes to clean towels daily. He missed one week of laundry. How many days the following week will Barney not have clean towels?"""
    # Define the number of towels Barney owns
    num_towels = 18

    # Define the number of towels used per day
    towels_per_day = 2

    # Define the number of days Barney missed washing his towels
    num_missed_weeks = 1

    # Calculate the number of towels used during the missed week
    num_missed_towels = towels_per_day * 7 * num_missed_weeks

    # Calculate the number of towels remaining after the missed week
    remaining_towels = num_towels - num_missed_towels

    # Calculate the number of days Barney can use the remaining towels
    num_usable_days = remaining_towels / towels_per_day

    # Calculate the number of days Barney will not have clean towels
    num_dirty_days = 7 - num_usable_days

    result = num_dirty_days
    return result

print(solution())