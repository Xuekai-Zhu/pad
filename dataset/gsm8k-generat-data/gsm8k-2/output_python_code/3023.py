def solution():
    """The weights of Christine's two cats are 7 and 10 pounds. What is her dog's weight if its weight is twice the sum of her two cats' weights?"""
    cat1_weight = 7
    cat2_weight = 10
    cats_weight_sum = cat1_weight + cat2_weight
    dog_weight = 2 * cats_weight_sum
    result = dog_weight
    return result

print(solution())