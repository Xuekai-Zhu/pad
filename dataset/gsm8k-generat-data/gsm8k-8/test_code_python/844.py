def solution():
    # Set up equation using variables for Rahim's current age (r) and Andy's current age (a)
    # In 5 years, Andy will be a+5, and at that time Rahim will be twice as old, or 2r
    # Therefore, a+5 = 2r
    # We also know Rahim's current age is 6, so r = 6
    r = 6
    a = 2*r - 5  # Solving for a using the equation above

    # Calculate the age difference between Andy and Rahim
    age_diff = a - r
    result = age_diff
    return result

print(solution())