def solution():
    """Randy had some money. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. If Randy has $2000 left, how much money, in dollars, did Randy have at first?"""
    # Randy's current amount of money
    current_amount = 2000

    # Randy gave $1200 to Sally
    current_amount += 1200

    # Randy kept the rest after giving $1200 to Sally
    remaining_amount = current_amount

    # Smith gave Randy $200
    remaining_amount -= 200

    # Randy's original amount of money
    original_amount = remaining_amount
    result = original_amount
    return result

print(solution())