def solution():
    
    cat_weights = [12, 12, 14.7, 9.3]
    total_weight = sum(cat_weights)
    num_cats = len(cat_weights)
    average_weight = total_weight / num_cats
    result = average_weight
    return result

print(solution())