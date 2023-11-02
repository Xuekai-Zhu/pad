def solution():
    back_squat_weight = 250  # 200 kg + 50 kg increase
    front_squat_weight = back_squat_weight * 0.8
    triple_weight = front_squat_weight * 0.9
    total_weight = triple_weight * 9
    result = total_weight
    return result

print(solution())