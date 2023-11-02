def solution():
    
    ajax_weight = 80 * 2.2  
    exercise_time = 2  
    weight_loss_per_hour = 1.5
    total_weight_loss = (weight_loss_per_hour * exercise_time) * 14  
    final_weight = ajax_weight - total_weight_loss
    result = final_weight
    return result

print(solution())