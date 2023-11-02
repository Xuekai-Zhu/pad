def solution():
    """CJ, KJ, and AJ collect stamps. CJ has 5 more than twice the number of stamps that KJ has, and KJ has half as many as AJ. If the three boys have 930 stamps all together, how many stamps does AJ have?"""
    # Let x be AJ's number of stamps
    x = 2 * (x / 2) + 5 + x
    
    # Total number of stamps
    total_stamps = x + x / 2 + 2 * (x / 2) + 5
    
    # Solve for x
    x = (930 - 5) / 2
    
    result = x
    
    return result

print(solution())