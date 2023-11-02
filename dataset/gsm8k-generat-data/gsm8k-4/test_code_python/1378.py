def solution():
    """Brenda weighs 10 pounds more than 3 times Mel's weight. If Brenda weighs 220 pounds, what is Mel's weight?"""
    # Define the weight of Brenda and the weight multiplier for Mel
    brenda_weight = 220
    mel_weight_multiplier = 1 / 3

    # Calculate Mel's weight using the given equation
    mel_weight = (brenda_weight - 10) * mel_weight_multiplier

    # Return Mel's weight
    result = mel_weight
    return result

print(solution())