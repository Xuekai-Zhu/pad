def solution():
    # Convert Ajax's weight from kg to pounds
    ajax_weight_pounds = 80 * 2.2

    # Calculate the weight loss per day
    weight_loss_per_hour = 1.5 / 2.2
    weight_loss_per_day = weight_loss_per_hour * 2  # Ajax exercises for 2 hours per day

    # Calculate the total weight loss in two weeks
    total_weight_loss = weight_loss_per_day * 14

    # Calculate Ajax's weight in pounds after two weeks of exercise
    ajax_weight_after_exercise = ajax_weight_pounds - total_weight_loss

    result = ajax_weight_after_exercise
    return result

print(solution())