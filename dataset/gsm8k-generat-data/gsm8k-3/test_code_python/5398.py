def solution():
    """John weighs 220 pounds when he starts exercising. He manages to lose 10% of his body weight. He then gains back 2 pounds. How much does he weigh at the end?"""
    # Define John's initial weight
    initial_weight = 220

    # Calculate the weight loss and resulting weight
    weight_loss = initial_weight * 0.1
    resulting_weight = initial_weight - weight_loss

    # Calculate the weight gain and resulting weight
    weight_gain = 2
    resulting_weight += weight_gain

    # Display John's final weight
    result = resulting_weight
    return result

print(solution())