def solution():
    """Wanda weighs 30 pounds more than Yola currently. Wanda also weighs 80 pounds more than Yola did 2 years ago. How much did Yola weigh 2 years ago if she currently weighs 220 pounds?"""
    # Calculate Yola's current weight
    yola_current_weight = 220

    # Calculate Wanda's current weight
    wanda_current_weight = yola_current_weight + 30

    # Calculate Yola's weight 2 years ago
    yola_2_years_ago = wanda_current_weight - 80

    # return the result
    result = yola_2_years_ago
    return result

print(solution())