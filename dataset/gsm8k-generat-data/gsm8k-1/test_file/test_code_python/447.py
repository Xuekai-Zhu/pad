def solution():
    """On a certain day, the total cost of filling up 20 helium balloons was $900. Two days later, the cost of filling each balloon was increased by $20. How much did Bentley pay to fill 170 balloons if he went to fill them after the price increase?"""
    original_cost = 900
    original_balloons = 20
    increased_cost_per_balloon = original_cost / original_balloons + 20
    new_balloons = 170
    total_cost = new_balloons * increased_cost_per_balloon
    result = total_cost
    return result

print(solution())