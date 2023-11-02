def solution():
    """Wanda weighs 30 pounds more than Yola currently. Wanda also weighs 80 pounds more than Yola did 2 years ago. How much did Yola weigh 2 years ago if she currently weighs 220 pounds?"""
    # Define Wanda's current weight and the weight difference between Wanda and Yola
    wanda_weight = 220
    weight_difference = 30

    # Calculate Yola's weight currently
    yola_weight = wanda_weight - weight_difference

    # Calculate Yola's weight 2 years ago
    yola_weight_2_years_ago = yola_weight - 80

    # Display Yola's weight 2 years ago
    result = yola_weight_2_years_ago
    return result

print(solution())