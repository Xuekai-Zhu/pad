def solution():
    """Lulu has $65 in her piggy bank. She spent $5 on ice cream. She then spent half of the remainder of the money on a t-shirt. Afterwards, she went to the bank and deposited a fifth of her remaining money. How much cash was Lulu left with?"""
    # Define the initial amount of money Lulu has
    initial_money = 65

    # Subtract the money spent on ice cream
    remaining_money = initial_money - 5

    # Calculate the amount spent on the t-shirt
    tshirt_cost = remaining_money / 2

    # Subtract the cost of the t-shirt
    remaining_money -= tshirt_cost

    # Calculate the amount deposited in the bank
    deposited_money = remaining_money / 5

    # Subtract the deposited money
    remaining_money -= deposited_money

    # return the result
    result = remaining_money
    return result

print(solution())