def solution():
    """James decides to bulk up.  He weighs 120 kg and gains 20% of his body weight in muscle and 1 quarter that much in fat.  How much does he weigh now?"""
    # Define James' starting weight
    weight = 120

    # Calculate the amount of weight gained in muscle
    muscle_gain = weight * 0.2

    # Calculate the amount of weight gained in fat
    fat_gain = muscle_gain / 4

    # Calculate James' new weight
    new_weight = weight + muscle_gain + fat_gain

    # Display James' new weight
    result = new_weight
    return result

print(solution())