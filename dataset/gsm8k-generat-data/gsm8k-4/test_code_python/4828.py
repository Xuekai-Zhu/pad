def solution():
    """John had $20. He spent 1/5 of his money on snacks and 3/4 of the remaining money on necessities. How much is left of John's money?"""
    # Define the initial amount of money John had
    initial_money = 20

    # Calculate the amount spent on snacks
    snacks_spending = initial_money * (1/5)

    # Calculate the remaining money after buying snacks
    remaining_money = initial_money - snacks_spending

    # Calculate the amount spent on necessities
    necessities_spending = remaining_money * (3/4)

    # Calculate the final amount of money remaining
    final_money = remaining_money - necessities_spending

    # return the result
    result = final_money
    return result

print(solution())