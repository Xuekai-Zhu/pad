def solution():
    """On Monday, while at work on the farm, Jeremy picks 100 oranges. On Tuesday, together with his brother, they pick thrice as much. On Wednesday he feels tired and is only able to pick 70 oranges. What's the total number of oranges they have?"""
    monday_oranges = 100
    tuesday_oranges = 3 * monday_oranges
    wednesday_oranges = 70
    total_oranges = monday_oranges + tuesday_oranges + wednesday_oranges
    result = total_oranges
    return result

print(solution())