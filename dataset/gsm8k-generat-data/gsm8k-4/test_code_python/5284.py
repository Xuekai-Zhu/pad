def solution():
    """Kelly has 8 chickens that lay 3 eggs each per day. If Kelly sells these eggs for $5 a dozen. How much money will she make in 4 weeks if she sells all her eggs?"""
    # Define the number of chickens and eggs per day
    CHICKENS = 8
    EGGS_PER_CHICKEN_PER_DAY = 3

    # Calculate the total number of eggs per day
    total_eggs_per_day = CHICKENS * EGGS_PER_CHICKEN_PER_DAY

    # Calculate the total number of eggs per week
    total_eggs_per_week = total_eggs_per_day * 7

    # Calculate the total number of eggs in 4 weeks
    total_eggs_in_4_weeks = total_eggs_per_week * 4

    # Calculate the number of dozens of eggs
    dozens_of_eggs = total_eggs_in_4_weeks / 12

    # Calculate the total money earned
    total_money_earned = dozens_of_eggs * 5

    # Return the result
    result = total_money_earned
    return result

print(solution())