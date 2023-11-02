def solution():
    """Markese earned 5 fewer dollars than Evan. Together they earned $37. How many dollars did Markese earn? Use E to represent how many dollars Evan earned."""
    # Define the amount of money Evan earned
    E = None
    
    # Calculate the amount of money Markese earned
    M = E - 5
    
    # Use the fact that together they earned $37 to solve for E and M
    E + M = 37
    E + (E-5) = 37
    2E - 5 = 37
    2E = 42
    E = 21
    
    # Calculate the amount of money Markese earned
    M = E - 5
    
    # Return the result
    result = M
    return result

print(solution())