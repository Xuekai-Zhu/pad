def solution():
    # Define the cost of each item and the total cost
    jersey_cost = 2
    basketball_cost = 18
    shorts_cost = 8
    total_cost = (5 * jersey_cost) + basketball_cost + shorts_cost

    # Calculate how much money Jeremy has left
    money_left = 50 - total_cost
    result = money_left
    return result

print(solution())