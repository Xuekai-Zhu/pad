def solution():
    """Tom originally was only able to lift 80 kg farmer handles per hand. After some training, he was able to double this number. He then decided to specialize and was able to get an extra 10%. How much weight can he hold in total?"""
    original_weight = 80
    doubled_weight = original_weight * 2
    specialized_weight = doubled_weight * 1.1
    total_weight = specialized_weight * 2
    result = total_weight
    return result

print(solution())