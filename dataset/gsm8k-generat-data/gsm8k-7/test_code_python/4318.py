def solution():
    num_coffee = 2
    coffee_price = 4

    num_cake = 1
    cake_price = 7

    num_icecream = 2
    icecream_price = 3

    # Calculate the total cost of coffee
    coffee_cost = num_coffee * coffee_price

    # Calculate the total cost of cake
    cake_cost = num_cake * cake_price

    # Calculate the total cost of ice cream
    icecream_cost = num_icecream * icecream_price

    # Calculate the total cost of all items ordered
    total_cost = coffee_cost + cake_cost + icecream_cost
    result = total_cost
    return result

print(solution())