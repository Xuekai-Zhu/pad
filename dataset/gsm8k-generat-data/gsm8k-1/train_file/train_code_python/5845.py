def solution():
    """John can front squat 80% as much as he back squats. He used to back squat 200 kg but increased that by 50 kg. He can do a triple equal to 90% of the amount he front squats. How much weight will he move if he does three triples?"""
    back_squat_max = 200
    increased_back_squat_max = back_squat_max + 50
    front_squat_max = back_squat_max * 0.8
    triple_weight = front_squat_max * 0.9
    weight_moved = triple_weight * 3
    result = weight_moved
    
    return result

print(solution())