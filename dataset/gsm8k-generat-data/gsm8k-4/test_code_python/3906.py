def solution():
    """Verna weighs 17 pounds more than Haley, and Verna weighs half as much as Sherry. If Haley weighs 103 pounds, how many pounds do Verna and Sherry weigh together?"""
    
    # Find Verna's weight
    verna_weight = 103 + 17
    
    # Find Sherry's weight
    sherry_weight = verna_weight * 2
    
    # Find the total weight of Verna and Sherry
    total_weight = verna_weight + sherry_weight
    
    result = total_weight
    return result

print(solution())