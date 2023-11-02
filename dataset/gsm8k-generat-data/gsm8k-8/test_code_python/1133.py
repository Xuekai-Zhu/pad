def solution():
    # Calculate the total amount of water needed
    total_water = 100 * 3

    # Calculate the number of bottles of water needed and the total cost
    num_bottles = total_water / 50
    total_cost = num_bottles * 2.5

    # Calculate the amount of money Marcus has and his change
    marcus_money = 2 * 10
    change = marcus_money - total_cost
    result = change
    return result

print(solution())