def solution():
    """Patrick buys a season pass for each of his sons to visit the local amusement park as often as they want. The passes were $100.00 each. The oldest son went to the park 35 times over the summer and the youngest went 15 times. What was the cost per trip to the park?"""
    # Define the cost of each season pass
    season_pass_cost = 100

    # Define the number of times each son visited the park
    oldest_son_visits = 35
    youngest_son_visits = 15

    # Calculate the total cost of the season passes
    total_cost = season_pass_cost * 2

    # Calculate the average cost per visit
    cost_per_visit = total_cost / (oldest_son_visits + youngest_son_visits)

    result = cost_per_visit
    return result

print(solution())