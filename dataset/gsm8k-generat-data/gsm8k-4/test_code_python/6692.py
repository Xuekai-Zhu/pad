def solution():
    """On Monday, while at work on the farm, Jeremy picks 100 oranges. On Tuesday, together with his brother, they pick thrice as much. On Wednesday he feels tired and is only able to pick 70 oranges. What's the total number of oranges they have?"""
    
    # Define the number of oranges picked on Monday
    monday_oranges = 100
    
    # Define the number of oranges picked on Tuesday, 3 times as much as Monday
    tuesday_oranges = 3 * monday_oranges
    
    # Define the number of oranges picked on Wednesday
    wednesday_oranges = 70
    
    # Sum up the number of oranges picked on all three days
    total_oranges = monday_oranges + tuesday_oranges + wednesday_oranges
    
    # return the result
    result = total_oranges
    return result

print(solution())