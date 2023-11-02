def solution():
    bonus = 1496

    # Calculate the amount allocated for the kitchen
    kitchen_share = bonus / 22

    # Calculate the amount allocated for holidays
    holiday_share = bonus / 4

    # Calculate the amount allocated for Christmas gifts for each child
    child_gift_share = bonus / 8 / 3

    # Calculate the total amount spent
    total_spent = kitchen_share + holiday_share + 3 * child_gift_share

    # Calculate the remaining amount
    remaining_amount = bonus - total_spent
    result = remaining_amount
    return result

print(solution())