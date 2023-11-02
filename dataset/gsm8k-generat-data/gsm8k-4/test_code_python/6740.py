def solution():
    """If Sally had $20 less, she would have $80. If Jolly has $20 more, she would have $70. How much money do Sally and Jolly have altogether?"""
    # Define the initial amounts for Sally and Jolly
    sally_amount = None
    jolly_amount = None

    # Use a system of equations to solve for the amounts of Sally and Jolly
    # If Sally had $20 less, she would have $80
    # sally_amount - 20 = 80
    sally_amount = 100

    # If Jolly has $20 more, she would have $70
    # jolly_amount + 20 = 70
    jolly_amount = 50

    # Calculate the total amount of money that Sally and Jolly have together
    total_amount = sally_amount + jolly_amount

    # Return the result
    result = total_amount
    return result

print(solution())