def solution():
    """John can front squat 80% as much as he back squats. He used to back squat 200 kg but increased that by 50 kg. He can do a triple equal to 90% of the amount he front squats. How much weight will he move if he does three triples?"""
    back_squat_weight = 200 + 50
    front_squat_weight = 0.8 * back_squat_weight
    triple_weight = 0.9 * front_squat_weight
    total_weight = 3 * triple_weight
    result = total_weight
    return result

print(solution())