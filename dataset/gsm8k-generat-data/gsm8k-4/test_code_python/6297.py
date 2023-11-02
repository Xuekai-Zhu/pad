def solution():
    """Jordan decides to start an exercise program when he weighs 250 pounds. For the first 4 weeks, he loses 3 pounds a week. After that, he loses 2 pounds a week for 8 weeks. How much does Jordan now weigh?"""
    # Define the initial weight
    initial_weight = 250

    # Calculate the weight loss for the first 4 weeks
    weight_loss_4_weeks = 3 * 4

    # Calculate the remaining weight loss after the first 4 weeks
    remaining_weeks = 8
    weight_loss_remaining = 2 * remaining_weeks

    # Calculate the final weight
    final_weight = initial_weight - weight_loss_4_weeks - weight_loss_remaining

    # return the result
    result = final_weight
    return result

print(solution())