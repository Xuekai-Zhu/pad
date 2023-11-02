def solution():
    """Tony has a terrible toothache and decides to buy some painkillers from the store. He picks up a bottle of 50 pills and takes them home. He takes 2 pills each day, three times a day for the first 2 days, before cutting this amount in half for the next 3 days. On the sixth day, he takes a final 2 pills in the morning and ends up feeling better. How many pills are left in the bottle?"""
    # Define the initial number of pills and the number of pills taken each day
    initial_pills = 50
    daily_pills = 2 * 3

    # Calculate the total number of pills taken during the first 2 days
    first_two_days_pills = daily_pills * 2

    # Calculate the total number of pills taken during the next 3 days when the dosage is cut in half
    next_three_days_pills = (daily_pills / 2) * 3

    # Calculate the total number of pills taken on the sixth day
    sixth_day_pills = 2

    # Calculate the total number of pills taken
    total_pills_taken = first_two_days_pills + next_three_days_pills + sixth_day_pills

    # Calculate the number of pills remaining in the bottle
    pills_remaining = initial_pills - total_pills_taken

    # Display the number of pills remaining in the bottle
    result = pills_remaining
    return result

print(solution())