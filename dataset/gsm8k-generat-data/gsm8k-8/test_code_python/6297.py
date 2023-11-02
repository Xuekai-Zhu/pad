def solution():
    # Define starting weight and weeks of weight loss
    starting_weight = 250
    week1_weight_loss = 3
    week2_weight_loss = 3
    week3_weight_loss = 3
    week4_weight_loss = 3
    week5_weight_loss = 2
    week6_weight_loss = 2
    week7_weight_loss = 2
    week8_weight_loss = 2
    total_weeks = 12

    # Calculate total weight loss
    weight_loss = (week1_weight_loss + week2_weight_loss + week3_weight_loss + week4_weight_loss +
                   week5_weight_loss + week6_weight_loss + week7_weight_loss + week8_weight_loss)

    # Calculate current weight
    current_weight = starting_weight - weight_loss

    return current_weight

print(solution())