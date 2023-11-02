def solution():
    """Tony has a terrible toothache and decides to buy some painkillers from the store.  He picks up a bottle of 50 pills and takes them home.  He takes 2 pills each day three times a day for the first 2 days, before cutting this amount in half for the next 3 days.  On the sixth day, he takes a final 2 pills in the morning and ends up feeling better.  How many pills are left in the bottle?"""
    # Define the number of pills Tony takes each day
    PILLS_PER_DAY = 6

    # Calculate the total number of pills Tony takes in the first 2 days
    pills_first_two_days = PILLS_PER_DAY * 2

    # Calculate the total number of pills Tony takes in the next 3 days
    pills_next_three_days = int(PILLS_PER_DAY * 1.5) * 3

    # Calculate the total number of pills Tony takes in the sixth day
    pills_sixth_day = PILLS_PER_DAY

    # Calculate the total number of pills Tony takes over the entire period
    total_pills = pills_first_two_days + pills_next_three_days + pills_sixth_day

    # Calculate the number of pills left in the bottle
    pills_left = 50 - total_pills

    # Display the number of pills left in the bottle
    result = pills_left
    return result

print(solution())