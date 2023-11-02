def solution():
    # Calculate the total cost of Paul's shopping
    bread_cost = 2
    butter_cost = 3
    juice_cost = 2 * bread_cost
    total_cost = bread_cost + butter_cost + juice_cost

    # Calculate how much money Paul had left after shopping
    money_left = 15 - total_cost
    result = money_left
    return result

print(solution())