def solution():
    """Tom weighs 150 kg. He manages to hold 1.5 times his weight in each hand while wearing a weight vest weighing half his weight. How much total weight was he moving with?"""
    # Define Tom's weight and the weight of his weight vest
    TOM_WEIGHT = 150
    VEST_WEIGHT = TOM_WEIGHT / 2

    # Calculate the weight Tom is holding in each hand
    HAND_WEIGHT = TOM_WEIGHT * 1.5

    # Calculate the total weight Tom is moving with
    total_weight = (HAND_WEIGHT * 2) + VEST_WEIGHT

    # Display the total weight
    result = total_weight
    return result

print(solution())