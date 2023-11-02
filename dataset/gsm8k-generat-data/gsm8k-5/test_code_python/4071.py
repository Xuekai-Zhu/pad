def solution():
    original_weight = 70  # Mr Cruz originally weighed 70 pounds
    first_month_gain = 20  # Mr Cruz gained 20 pounds in the first month
    second_month_gain = 30  # Mr Cruz gained 30 pounds in the second month

    # Calculate Mr Cruz's weight after the first month
    weight_after_first_month = original_weight + first_month_gain

    # Calculate Mr Cruz's weight after the second month
    weight_after_second_month = weight_after_first_month + second_month_gain
    result = weight_after_second_month
    return result

print(solution())