def solution():
    cat_weight_1 = 7  # weight of the first cat in pounds
    cat_weight_2 = 10  # weight of the second cat in pounds

    # Calculate the sum of the weights of Christine's cats
    cat_weight_sum = cat_weight_1 + cat_weight_2

    # Calculate twice the sum of the weights of Christine's cats
    twice_cat_weight_sum = 2 * cat_weight_sum

    # Calculate the weight of Christine's dog
    dog_weight = twice_cat_weight_sum

    result = dog_weight
    return result

print(solution())