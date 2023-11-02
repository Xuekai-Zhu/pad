def solution():
    initial_money = 100  # Jack starts with $100
    num_bottles = 4  # Jack initially buys 4 bottles of water
    bottle_price = 2  # Each bottle costs $2
    additional_bottles = 2*num_bottles  # Jack buys twice as many additional bottles
    cheese_price = 10  # 1 pound of cheese costs $10
    cheese_amount = 0.5  # Jack buys half a pound of cheese

    # Calculate the total cost of the additional bottles and cheese
    additional_cost = additional_bottles*bottle_price + cheese_amount*cheese_price

    # Calculate the remaining money
    remaining_money = initial_money - additional_cost
    result = remaining_money
    return result

print(solution())