def solution():
    """Jack is mad at his neighbors for blasting Taylor Swift all night, so he slashes three of their tires and smashes their front window. If the tires cost $250 each and the window costs $700, how much will Jack have to pay for the damages?"""
    cost_per_tire = 250
    num_tires_slashed = 3
    cost_of_window = 700
    total_cost = (cost_per_tire * num_tires_slashed) + cost_of_window
    result = total_cost
    return result

print(solution())