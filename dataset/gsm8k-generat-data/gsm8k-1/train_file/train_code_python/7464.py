def solution():
    """James decides to bulk up. He weighs 120 kg and gains 20% of his body weight in muscle and 1 quarter that much in fat. How much does he weigh now?"""
    original_weight = 120
    muscle_gain_percent = 20
    fat_gain_percent = muscle_gain_percent / 4
    
    muscle_gain = original_weight * (muscle_gain_percent / 100)
    fat_gain = original_weight * (fat_gain_percent / 100)
    
    new_weight = original_weight + muscle_gain + fat_gain
    result = new_weight
    return result

print(solution())