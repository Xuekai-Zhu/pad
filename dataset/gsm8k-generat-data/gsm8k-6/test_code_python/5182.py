def solution():
    # Calculate the total cost of the 3 magic wands
    total_cost = 130 / 2  # Kate sold two wands to her friends
    cost_per_wand = (total_cost / 3) - 5  # Kate bought 3 wands, and sold them for $5 more each
    result = cost_per_wand
    return result

print(solution())