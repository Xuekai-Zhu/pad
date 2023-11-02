def solution():
    
    total_clovers = 500
    four_leaves_percent = 20
    purple_percent = 25
    
    
    four_leaves = (four_leaves_percent / 100) * total_clovers
    
    
    purple_clovers = (purple_percent / 100) * four_leaves
    
    
    result = purple_clovers
    return result

print(solution())