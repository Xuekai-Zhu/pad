def solution():
    """Ben will receive a bonus of $1496. He chooses to allocate this amount as follows: 1/22 for the kitchen, 1/4 for holidays and 1/8 for Christmas gifts for his 3 children. How much money will he still have left after these expenses?"""
    # Define the total bonus amount
    total_bonus = 1496

    # Calculate the amount allocated for the kitchen
    kitchen_allocation = total_bonus * (1/22)

    # Calculate the amount allocated for holidays
    holidays_allocation = total_bonus * (1/4)

    # Calculate the amount allocated for Christmas gifts for each child
    child_allocation = total_bonus * (1/8) / 3

    # Calculate the total amount spent
    total_spent = kitchen_allocation + holidays_allocation + child_allocation

    # Calculate the amount remaining
    amount_remaining = total_bonus - total_spent

    result = amount_remaining
    return result

print(solution())