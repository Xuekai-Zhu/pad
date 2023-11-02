def solution():
    """In January, Bill's labrador puppy weighs 40 pounds and his dachshund puppy weighs 12 pounds. Each dog gains 25% of their starting weight over the year. What's the difference in their weight at the end of the year?"""
    # Define the starting weights of the puppies
    labrador_start = 40
    dachshund_start = 12

    # Calculate the amount gained by each puppy
    labrador_gain = labrador_start * 0.25
    dachshund_gain = dachshund_start * 0.25

    # Add the gains to the starting weights to get the final weights
    labrador_final = labrador_start + labrador_gain
    dachshund_final = dachshund_start + dachshund_gain

    # Calculate the difference in their weights
    weight_difference = labrador_final - dachshund_final

    # Round the weight difference to one decimal place
    result = round(weight_difference, 1)
    return result

print(solution())