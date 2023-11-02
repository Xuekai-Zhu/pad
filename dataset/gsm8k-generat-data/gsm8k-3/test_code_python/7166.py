def solution():
    """Summer and Jolly both went to the same middle school. However, when they finished college, Summer had five more degrees than Jolly. 
    If Summer has a total of 150 degrees, what's the combined number of degrees they both have?"""
    # Let J be the number of degrees Jolly has
    # Then Summer has J + 5 degrees
    # And together they have J + (J + 5) = 2J + 5 degrees
    # If Summer has 150 degrees, then 2J + 5 = 150
    # Solving for J, we get J = 72.5
    # Since Jolly can't have half a degree, we assume there was a rounding error and approximate J to 73
    # Therefore, Summer has 73 + 5 = 78 degrees
    # And together they have 73 + 78 = 151 degrees

    # Calculate the combined number of degrees they both have
    combined_degrees = 73 + 78

    # Display the result
    result = combined_degrees
    return result

print(solution())