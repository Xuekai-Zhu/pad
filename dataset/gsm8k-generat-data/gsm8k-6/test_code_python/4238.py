def solution():
    # Calculate the cost of the sandwich after discount and upgrade
    sandwich_price = 8 - (8 / 4) + 1  # 25% discount and $1 upgrade for avocado

    # Calculate the total cost of the lunch
    total_cost = sandwich_price + 3 + 12 - 8  # cost of salad and drink plus cost of sandwich after discount

    # Calculate the cost of the drink
    drink_cost = total_cost - sandwich_price - 3  # subtract the cost of salad and sandwich from total cost

    result = drink_cost
    return result

print(solution())