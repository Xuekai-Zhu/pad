def solution():
    money_given = 74
    num_bread = 5
    bread_price = 5
    num_orange_juice = 4
    orange_juice_price = 2

    # Calculate the total cost of all bread
    total_bread_cost = num_bread * bread_price

    # Calculate the total cost of all orange juice
    total_orange_juice_cost = num_orange_juice * orange_juice_price

    # Calculate the total cost of all items Wyatt bought
    total_cost = total_bread_cost + total_orange_juice_cost

    # Calculate how much money Wyatt has left
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())