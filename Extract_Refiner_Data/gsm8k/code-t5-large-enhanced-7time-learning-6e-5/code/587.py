def solution():
    
    # Define the weights of the dogs
    affenpinscher_weight = 10
    dachshund_weight = 2 * affenpinscher_weight
    papillon_weight = dachshund_weight / 4
    mastiff_weight = 44 * papillon_weight

    # Calculate the total weight of the dogs
    total_weight = affenpinscher_weight + dachshund_weight + papillon_weight + mastiff_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())