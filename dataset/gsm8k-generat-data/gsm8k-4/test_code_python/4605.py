def solution():
    """Jane runs a small farm. She has 10 chickens that lay 6 eggs each per week. She can sell the eggs for $2/dozen. How much money will she make in 2 weeks if she sells all her eggs?"""
    # Define the number of chickens and eggs per week
    num_chickens = 10
    eggs_per_week = num_chickens * 6

    # Calculate the number of eggs over two weeks
    eggs_per_two_weeks = eggs_per_week * 2

    # Calculate the number of dozens of eggs
    dozens_of_eggs = eggs_per_two_weeks / 12

    # Calculate the total earnings
    earnings = dozens_of_eggs * 2

    result = earnings
    return result

print(solution())