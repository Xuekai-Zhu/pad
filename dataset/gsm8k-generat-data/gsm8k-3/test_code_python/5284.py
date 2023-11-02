def solution():
    """Kelly has 8 chickens that lay 3 eggs each per day. If Kelly sells these eggs for $5 a dozen. How much money will she make in 4 weeks if she sells all her eggs?"""
    # Define the number of chickens and eggs laid per day
    CHICKENS = 8
    EGGS_PER_CHICKEN = 3

    # Calculate the total number of eggs laid per day
    total_eggs = CHICKENS * EGGS_PER_CHICKEN

    # Calculate the total number of eggs laid in 4 weeks (28 days)
    total_eggs_4_weeks = total_eggs * 28

    # Calculate the total number of dozens of eggs
    total_dozens = total_eggs_4_weeks / 12

    # Calculate Kelly's earnings
    earnings = total_dozens * 5

    # Display Kelly's earnings
    result = round(earnings, 2)
    return result

print(solution())