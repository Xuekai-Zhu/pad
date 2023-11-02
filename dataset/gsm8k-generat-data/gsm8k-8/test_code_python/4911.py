def solution():
    # Convert Ajax's weight from kg to pounds
    ajax_weight_lbs = 80 * 2.2

    # Calculate the weight lost in 2 weeks (14 days) by exercising for 2 hours every day
    weight_lost_lbs = 14 * 2 * 1.5

    # Calculate the final weight in pounds
    final_weight_lbs = ajax_weight_lbs - weight_lost_lbs

    # Convert the final weight from pounds to kg
    final_weight_kg = final_weight_lbs / 2.2
    result = final_weight_kg
    return result

print(solution())