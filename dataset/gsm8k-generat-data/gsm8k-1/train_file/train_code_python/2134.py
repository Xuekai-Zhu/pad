def solution():
    """Janele wants to figure out the average weight of her cats. She has 4 of them. The first two weigh 12 pounds each. The third weighs 14.7 pounds and the fourth weighs 9.3 pounds. What is their average weight?"""
    num_cats = 4
    weight_cat1 = 12
    weight_cat2 = 12
    weight_cat3 = 14.7
    weight_cat4 = 9.3
    total_weight = weight_cat1 + weight_cat2 + weight_cat3 + weight_cat4
    avg_weight = total_weight / num_cats
    result = avg_weight
    return result

print(solution())