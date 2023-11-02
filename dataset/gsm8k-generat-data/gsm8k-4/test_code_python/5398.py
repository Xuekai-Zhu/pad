def solution():
    """John weighs 220 pounds when he starts exercising. He manages to lose 10% of his body weight. He then gains back 2 pounds. How much does he weigh at the end?"""
    # Define John's initial weight
    initial_weight = 220

    # Calculate the weight lost
    weight_lost = initial_weight * 0.1

    # Calculate John's weight after losing weight
    weight_after_loss = initial_weight - weight_lost

    # Add 2 pounds to his weight after losing weight
    final_weight = weight_after_loss + 2

    result = final_weight
    return result

print(solution())