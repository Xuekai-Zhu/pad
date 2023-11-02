def solution():
    start_weight = 300
    month_one_loss = 20
    end_weight = 250.5

    # Calculate the total weight lost in months 2-4
    month_two_loss = month_one_loss / 2
    month_three_loss = month_two_loss / 2
    month_four_loss = month_three_loss / 2
    total_weight_lost = month_one_loss + month_two_loss + month_three_loss + month_four_loss

    # Calculate the weight lost in the fifth month
    target_weight = end_weight + total_weight_lost
    month_five_loss = target_weight - (start_weight - total_weight_lost)
    result = month_five_loss
    return result

print(solution())