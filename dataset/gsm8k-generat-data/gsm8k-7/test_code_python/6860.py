def solution():
    starting_weight = 250
    weight_loss_per_month = 8
    num_months = 12

    # Calculate the total weight loss after one year
    total_weight_loss = weight_loss_per_month * num_months

    # Calculate Calvin's weight after one year
    final_weight = starting_weight - total_weight_loss
    result = final_weight
    return result

print(solution())