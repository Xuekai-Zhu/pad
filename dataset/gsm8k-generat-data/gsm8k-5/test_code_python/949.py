def solution():
    current_weight_yola = 220  # Yola currently weighs 220 pounds
    weight_difference = 30  # Wanda weighs 30 pounds more than Yola currently
    wanda_weight_2_years_ago = current_weight_yola - weight_difference - 80  # Wanda currently weighs 80 pounds more than Yola did 2 years ago
    yola_weight_2_years_ago = wanda_weight_2_years_ago - weight_difference  # Yola weighed 30 pounds less than Wanda 2 years ago

    result = yola_weight_2_years_ago
    return result

print(solution())