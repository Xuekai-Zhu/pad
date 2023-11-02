def solution():
    """Wanda weighs 30 pounds more than Yola currently. Wanda also weighs 80 pounds more than Yola did 2 years ago. How much did Yola weigh 2 years ago if she currently weighs 220 pounds?"""
    current_weight_yola = 220
    weight_difference = 30
    wanda_weight_2_years_ago = current_weight_yola - weight_difference - 80
    yola_weight_2_years_ago = wanda_weight_2_years_ago - weight_difference
    
    result = yola_weight_2_years_ago
    
    return result

print(solution())