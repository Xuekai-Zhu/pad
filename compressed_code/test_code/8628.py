def solution():
    
    investment = 400
    first_week_gain = investment * 0.25
    first_week_value = investment + first_week_gain
    second_week_gain = first_week_value * 0.5
    final_value = first_week_value + second_week_gain
    result = final_value
    return result

print(solution())