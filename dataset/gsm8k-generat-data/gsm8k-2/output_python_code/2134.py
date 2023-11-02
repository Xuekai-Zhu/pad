def solution():
    """Janele wants to figure out the average weight of her cats. She has 4 of them. The first two weigh 12 pounds each. The third weighs 14.7 pounds and the fourth weighs 9.3 pounds. What is their average weight?"""
    cat_weights = [12, 12, 14.7, 9.3]
    total_weight = sum(cat_weights)
    num_cats = len(cat_weights)
    average_weight = total_weight / num_cats
    result = average_weight
    return result

print(solution())