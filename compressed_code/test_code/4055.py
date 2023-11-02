def solution():
    
    base_squat = 135
    training_increase = 265
    total_weight = base_squat + training_increase
    bracer_increase = total_weight * 6
    final_weight = total_weight + bracer_increase
    result = final_weight
    return result

print(solution())