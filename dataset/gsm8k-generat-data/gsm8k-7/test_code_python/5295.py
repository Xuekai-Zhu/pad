def solution():
    num_sandwiches = 3
    sandwich_price = 5
    money_paid = 20

    # Calculate the total cost of all sandwiches
    total_cost = num_sandwiches * sandwich_price

    # Calculate the change Jack will receive
    change = money_paid - total_cost
    result = change
    return result

print(solution())