def solution():
    # Calculate the weight of the labrador puppy after a year
    labrador_weight = 40 + (0.25 * 40)  # Labrador puppy gains 25% of their starting weight

    # Calculate the weight of the dachshund puppy after a year
    dachshund_weight = 12 + (0.25 * 12)  # Dachshund puppy gains 25% of their starting weight

    # Calculate the difference in weight between the two puppies after a year
    weight_difference = labrador_weight - dachshund_weight
    result = weight_difference
    return result

print(solution())