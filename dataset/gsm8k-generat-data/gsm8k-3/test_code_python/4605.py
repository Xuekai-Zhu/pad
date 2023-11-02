def solution():
    """Jane runs a small farm.  She has 10 chickens that lay 6 eggs each per week. She can sell the eggs for $2/dozen.  How much money will she make in 2 weeks if she sells all her eggs?"""
    # Define the number of chickens and number of eggs laid per chicken per week
    NUM_CHICKENS = 10
    EGGS_PER_CHICKEN_PER_WEEK = 6

    # Calculate the total number of eggs laid in 2 weeks
    total_eggs = NUM_CHICKENS * EGGS_PER_CHICKEN_PER_WEEK * 2

    # Calculate the number of dozens of eggs
    dozens = total_eggs / 12

    # Calculate the total amount of money Jane will make
    total_money = dozens * 2

    # Display the total amount of money
    result = total_money
    return result

print(solution())