def solution():
    front_squat_ratio = 0.80
    back_squat_increase = 50
    back_squat_amount = 200 + back_squat_increase
    front_squat_amount = front_squat_ratio * back_squat_amount
    triple_ratio = 0.90
    triple_amount = triple_ratio * front_squat_amount
    total_weight = triple_amount * 3
    result = total_weight
    return result

print(solution())