def solution():
    """Ryan’s allowance is $6 each week he completes his chores. He did his chores for 3 weeks. Then he bought ice cream cones for himself and 3 friends at $1.25 each. Now they all want to go to the movies and tickets cost $6.50 each. How many movie tickets can Ryan buy?"""
    allowance_per_week = 6
    weeks_completed = 3
    total_allowance = allowance_per_week * weeks_completed
    ice_cream_cost = 1.25 * 4
    total_cost = ice_cream_cost + (6.5 * x)
    x = (total_allowance - ice_cream_cost) // 6.5
    result = x
    return result

print(solution())