def solution():
    labrador_weight = 40  # Labrador puppy weighs 40 pounds in January
    dachshund_weight = 12  # Dachshund puppy weighs 12 pounds in January

    # Calculate the weight gain for each puppy
    labrador_gain = labrador_weight * 0.25
    dachshund_gain = dachshund_weight * 0.25

    # Add the weight gain to the starting weight for each puppy
    labrador_end_weight = labrador_weight + labrador_gain
    dachshund_end_weight = dachshund_weight + dachshund_gain

    # Calculate the difference in weight between the two puppies
    weight_difference = labrador_end_weight - dachshund_end_weight
    result = weight_difference
    return result

print(solution())