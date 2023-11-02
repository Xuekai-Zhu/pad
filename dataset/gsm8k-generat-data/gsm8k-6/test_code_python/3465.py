def solution():
    # Calculate the total cost of bread and orange juice
    bread_cost = 5 * 5  # Each bread loaf cost $5 and Wyatt bought 5 loaves of bread
    juice_cost = 4 * 2  # Each carton of orange juice cost $2 and Wyatt bought 4 cartons of orange juice
    total_cost = bread_cost + juice_cost  # Total cost of bread and juice

    # Calculate the remaining amount of money Wyatt has after buying bread and juice
    remaining_money = 74 - total_cost  
    result = remaining_money
    return result

print(solution())