def solution():
    """James decides to bulk up. He weighs 120 kg and gains 20% of his body weight in muscle and 1 quarter that much in fat. How much does he weigh now?"""
    initial_weight = 120
    muscle_gain = initial_weight * 0.2
    fat_gain = muscle_gain * 0.25
    total_gain = muscle_gain + fat_gain
    final_weight = initial_weight + total_gain
    result = final_weight
    return result

print(solution())