def solution():
    # Calculate the total cost of the purchases
    dress_cost = 20 * 5
    pants_cost = 12 * 3
    jacket_cost = 30 * 4
    total_cost = dress_cost + pants_cost + jacket_cost + 5

    # Calculate how much money Rita has left
    initial_money = 400
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())