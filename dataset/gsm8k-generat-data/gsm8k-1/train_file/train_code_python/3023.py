def solution():
    """The weights of Christine's two cats are 7 and 10 pounds. What is her dog's weight if its weight is twice the sum of her two cats' weights?"""
    cat1_weight = 7
    cat2_weight = 10
    sum_of_cats = cat1_weight + cat2_weight
    dog_weight = sum_of_cats * 2
    result = dog_weight
    return result

print(solution())