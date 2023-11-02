def solution():
    initial_weight = 80
    weight_loss_per_hour = 1.5 / 2.2  # convert pound to kilogram
    num_hours_per_day = 2
    num_days = 14

    # Calculate the total weight loss after two weeks
    total_weight_loss = weight_loss_per_hour * num_hours_per_day * num_days

    # Calculate the final weight in kilogram
    final_weight = initial_weight - total_weight_loss

    # Convert final weight to pounds
    final_weight_in_pounds = final_weight * 2.2
    result = final_weight_in_pounds
    return result

print(solution())