def solution():
    """James decides to bulk up. He weighs 120 kg and gains 20% of his body weight in muscle and 1 quarter that much in fat. How much does he weigh now?"""
    # Define James' initial weight
    james_weight = 120

    # Calculate the amount of muscle James gains
    muscle_gain = james_weight * 0.2

    # Calculate the amount of fat James gains
    fat_gain = muscle_gain / 4

    # Calculate James' new weight
    james_new_weight = james_weight + muscle_gain + fat_gain

    result = james_new_weight
    return result

print(solution())