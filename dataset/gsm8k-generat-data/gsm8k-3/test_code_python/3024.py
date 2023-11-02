def solution():
    """The weights of Christine's two cats are 7 and 10 pounds. What is her dog's weight if its weight is twice the sum of her two cats' weights?"""
    # Define the weights of Christine's two cats
    cat1_weight = 7
    cat2_weight = 10

    # Calculate the sum of the weights of the two cats
    cat_weight_sum = cat1_weight + cat2_weight

    # Calculate the weight of Christine's dog
    dog_weight = cat_weight_sum * 2

    # Display the weight of the dog
    result = dog_weight
    return result

print(solution())