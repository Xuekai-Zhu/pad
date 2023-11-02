def solution():
    """John had $20. He spent 1/5 of his money on snacks and 3/4 of the remaining money on necessities. How much is left of John's money?"""
    # Define John's initial amount of money
    john_money = 20

    # Calculate the amount spent on snacks
    snacks_spent = john_money * (1/5)

    # Calculate the remaining amount of money
    remaining_money = john_money - snacks_spent

    # Calculate the amount spent on necessities
    necessities_spent = remaining_money * (3/4)

    # Calculate the final amount of money remaining
    final_money = remaining_money - necessities_spent

    # Display the final amount of money remaining
    result = final_money
    return result

print(solution())