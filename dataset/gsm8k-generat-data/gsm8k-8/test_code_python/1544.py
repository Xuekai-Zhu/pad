def solution():
    # Define the bonus amount
    bonus = 1496

    # Calculate the amounts allocated to each expense
    kitchen_amount = bonus / 22
    holiday_amount = bonus / 4
    children_amount = bonus / 8 / 3

    # Calculate the total amount spent
    total_spent = kitchen_amount + holiday_amount + children_amount

    # Calculate the amount left over
    amount_left = bonus - total_spent
    result = amount_left
    return result

print(solution())