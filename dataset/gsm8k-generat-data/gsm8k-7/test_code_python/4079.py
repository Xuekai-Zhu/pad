def solution():
    initial_money = 47
    num_bread = 4
    bread_price = 2
    num_milk = 2
    milk_price = 2

    # Calculate the total cost of all bread
    total_bread_cost = num_bread * bread_price

    # Calculate the total cost of all milk
    total_milk_cost = num_milk * milk_price

    # Calculate the total cost of all items
    total_cost = total_bread_cost + total_milk_cost

    # Calculate the amount of money left after buying all items
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())