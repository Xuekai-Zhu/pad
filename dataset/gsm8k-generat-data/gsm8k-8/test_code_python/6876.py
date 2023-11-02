def solution():
    # Calculate the total cost of the food
    food_cost = 2*24 + 2*3.5 + 3*2

    # Calculate the amount of money Selena will have left after paying for food
    left_over_money = 99 - food_cost

    result = left_over_money
    return result

print(solution())