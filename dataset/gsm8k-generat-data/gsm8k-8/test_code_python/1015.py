def solution():
    # Calculate the number of oranges Timmy needs to buy
    oranges_needed = 400 / 80

    # Calculate the total cost of the oranges
    total_cost = oranges_needed * 1.20

    # Calculate the amount of money Timmy will have left
    money_left = 10 - total_cost
    result = money_left
    return result

print(solution())