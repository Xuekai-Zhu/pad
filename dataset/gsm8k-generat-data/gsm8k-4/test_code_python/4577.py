def solution():
    """Augustus can make 3 milkshakes per hour while Luna can make 7 milkshakes per hour. If Augustus and Luna have been making milkshakes for 8 hours now, how many milkshakes have they made?"""
    # Define the milkshake production rate for Augustus and Luna
    augustus_rate = 3
    luna_rate = 7

    # Define the number of hours they have been making milkshakes
    hours = 8

    # Calculate the total number of milkshakes made by Augustus and Luna
    total_milkshakes = (augustus_rate + luna_rate) * hours

    # Return the result
    result = total_milkshakes
    return result

print(solution())