def solution():
    lunch_cost = 10
    ice_cream_cost = 5

    # Calculate the total amount of money Randy spent
    total_spent = lunch_cost + ice_cream_cost

    # Calculate the amount of money Randy had left after buying lunch
    money_left = total_spent / 3  # since he spent a quarter of what he had left on ice cream

    # Calculate the amount of money Randy had at first
    initial_money = total_spent + money_left
    result = initial_money
    return result

print(solution())