def solution():
    """Lulu has $65 in her piggy bank. She spent $5 on ice cream. She then spent half of the remainder of the money on a t-shirt. Afterwards, she went to the bank and deposited a fifth of her remaining money. How much cash was Lulu left with?"""
    # Define the initial amount of money Lulu has
    initial_amount = 65

    # Deduct the cost of ice cream
    remaining_amount = initial_amount - 5

    # Deduct half of the remaining amount for the t-shirt
    remaining_amount = remaining_amount/2

    # Deposit a fifth of the remaining amount
    remaining_amount = remaining_amount * 0.8

    # Display the amount of money Lulu is left with
    result = remaining_amount
    return result

print(solution())