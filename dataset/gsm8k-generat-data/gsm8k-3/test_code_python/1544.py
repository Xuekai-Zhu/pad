def solution():
    """Ben will receive a bonus of $1496. He chooses to allocate this amount as follows: 1/22 for the kitchen, 1/4 for holidays and 1/8 for Christmas gifts for his 3 children. How much money will he still have left after these expenses?"""
    # Define the bonus amount
    bonus = 1496

    # Calculate the amount allocated for the kitchen
    kitchen_share = bonus * (1/22)

    # Calculate the amount allocated for holidays
    holiday_share = bonus * (1/4)

    # Calculate the amount allocated for Christmas gifts for each child
    child_gift_share = bonus * (1/8) / 3

    # Calculate the total amount spent
    total_spent = kitchen_share + holiday_share + child_gift_share

    # Calculate the amount Ben still has left
    remaining_amount = bonus - total_spent

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())