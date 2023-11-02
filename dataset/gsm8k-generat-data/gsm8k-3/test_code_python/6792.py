def solution():
    """In January, Bill's labrador puppy weighs 40 pounds and his dachshund puppy weighs 12 pounds. Each dog gains 25% of their starting weight over the year. What's the difference in their weight at the end of the year?"""
    # Define the starting weights of the labrador and dachshund puppies
    labrador_weight = 40
    dachshund_weight = 12

    # Calculate the weight gain for each puppy
    labrador_gain = labrador_weight * 0.25
    dachshund_gain = dachshund_weight * 0.25

    # Calculate the weight of each puppy at the end of the year
    labrador_end_weight = labrador_weight + labrador_gain
    dachshund_end_weight = dachshund_weight + dachshund_gain

    # Calculate the difference in weight between the two puppies at the end of the year
    weight_diff = labrador_end_weight - dachshund_end_weight

    # Display the weight difference
    result = weight_diff
    return result

print(solution())