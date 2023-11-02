def solution():
    """On Monday, while at work on the farm, Jeremy picks 100 oranges. On Tuesday, together with his brother, they pick thrice as much. On Wednesday he feels tired and is only able to pick 70 oranges. What's the total number of oranges they have?"""
    # Define the number of oranges picked on each day
    monday_oranges = 100
    tuesday_oranges = monday_oranges * 3
    wednesday_oranges = 70

    # Calculate the total number of oranges picked
    total_oranges = monday_oranges + tuesday_oranges + wednesday_oranges

    # Display the total number of oranges
    result = total_oranges
    return result

print(solution())