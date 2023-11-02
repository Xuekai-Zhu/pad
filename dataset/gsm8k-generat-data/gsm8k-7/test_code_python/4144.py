def solution():
    total_money = 32
    bread_price = 3
    candy_price = 2

    # Calculate the money spent on bread and candy
    total_spent = bread_price + candy_price

    # Calculate the remaining money after purchasing bread and candy
    remaining_money = total_money - total_spent

    # Calculate the cost of 1/3 of the remaining money spent on turkey
    turkey_cost = remaining_money / 3

    # Calculate the remaining money after purchasing turkey
    remaining_money = remaining_money - turkey_cost

    result = remaining_money
    return result

print(solution())