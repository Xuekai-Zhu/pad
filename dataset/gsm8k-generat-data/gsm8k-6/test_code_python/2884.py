def solution():
    # Find the weight of Felix
    weight_Felix = x  # let x be Felix's weight
    # Find the weight of Felix's brother
    weight_brother = 2 * weight_Felix
    # Find the lifting capacity of Felix and his brother
    lifting_capacity_brother = 3 * weight_brother
    # Find how much Felix can lift off the ground
    lifting_capacity_Felix = lifting_capacity_brother / (1.5 * weight_Felix)
    result = lifting_capacity_Felix
    return result

print(solution())