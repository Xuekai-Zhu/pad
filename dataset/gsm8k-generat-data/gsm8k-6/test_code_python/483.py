def solution():
    # First, calculate Andy's new weight after growing and gaining weight
    new_weight = 156 + 36
    # Convert Andy's height to inches
    height_inches = 3 * 12
    # Calculate his BMI at the beginning of the year
    bmi_start = new_weight / (height_inches ** 2) * 703
    # Calculate how much Andy lost each month
    weight_loss_per_month = new_weight / 8
    # Calculate Andy's weight after 3 months of losing weight
    weight_loss_3_months = 3 * weight_loss_per_month
    final_weight = new_weight - weight_loss_3_months
    # Calculate the difference between the final weight and the weight at the beginning of the year
    weight_difference = new_weight - final_weight
    result = weight_difference
    return result

print(solution())