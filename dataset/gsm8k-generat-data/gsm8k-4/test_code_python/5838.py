def solution():
    """Mark and Peter dug ponds in their backyards. Mark’s pond is 4 feet deeper than 3 times Peter’s pond. If Mark’s pond is 19 feet deep, what is the depth of Peter’s pond?"""
    # Let Peter's pond depth be x
    # Mark’s pond depth is 4 feet deeper than 3 times Peter’s pond
    # So Mark's pond depth = 3x + 4
    
    # Mark's pond depth is given as 19 feet
    mark_depth = 19
    
    # By substituting the above values, we get:
    3x + 4 = 19
    
    # Solving the above equation, we get:
    x = 5
    
    # Therefore, Peter's pond depth is 5 feet
    result = x
    return result

print(solution())