def solution():
    """Wanda weighs 30 pounds more than Yola currently. Wanda also weighs 80 pounds more than Yola did 2 years ago. How much did Yola weigh 2 years ago if she currently weighs 220 pounds?"""
    wanda_weight = 220
    yola_weight_2_years_ago = (wanda_weight - 80) - 30
    result = yola_weight_2_years_ago
    return result

print(solution())