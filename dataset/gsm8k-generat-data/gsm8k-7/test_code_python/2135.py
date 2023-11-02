def solution():
    num_cats = 4
    weight_cat1 = 12
    weight_cat2 = 12
    weight_cat3 = 14.7
    weight_cat4 = 9.3

    # Calculate the total weight of all cats
    total_weight = weight_cat1 + weight_cat2 + weight_cat3 + weight_cat4

    # Calculate the average weight of all cats
    avg_weight = total_weight / num_cats
    result = avg_weight
    return result

print(solution())