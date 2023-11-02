def solution():
    """Randy had some money. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. If Randy has $2000 left, how much money, in dollars, did Randy have at first?"""
    # Define the initial amount of money Randy had
    initial_money = None

    # Define the amount of money Smith gave Randy
    smith_money = 200

    # Calculate the amount of money Randy had after Smith gave him money
    randy_money = initial_money + smith_money

    # Calculate the amount of money Randy had left after giving money to Sally
    randy_money_left = randy_money - 1200

    # Calculate the initial amount of money Randy had
    initial_money = randy_money_left + 2000

    result = initial_money
    return result

print(solution())