def solution():
    # Calculate the total cost of the baguettes and water
    baguette_cost = 2 * 2  # 2 baguettes at $2 each
    water_cost = 2 * 1  # 2 bottles of water at $1 each
    total_cost = baguette_cost + water_cost

    # Calculate how much money Kenneth has left
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())