def solution():
    starting_money = 26
    jumper_price = 9
    tshirt_price = 4
    heels_price = 5

    # Calculate the total cost of all items
    total_cost = jumper_price + tshirt_price + heels_price

    # Calculate the remaining money after shopping
    remaining_money = starting_money - total_cost
    result = remaining_money
    return result

print(solution())