def solution():
    """Ajax is 80 kilograms. He is planning to lose some weight. Exercising for an hour will help him lose 1.5 pounds. If 1 kilogram is equal to 2.2 pounds How many pounds will he weigh if he exercises for 2 hours every day for two weeks?"""
    # Define Ajax's initial weight and the weight loss per hour of exercising
    initial_weight = 80
    loss_per_hour = 1.5 / 2.2

    # Calculate the total weight loss after exercising for 2 hours every day for 2 weeks
    total_hours = 2 * 7 * 2
    total_weight_loss = total_hours * loss_per_hour

    # Calculate Ajax's weight after the weight loss
    final_weight = initial_weight - (total_weight_loss / 2.2)

    # Round the weight to 2 decimal places
    final_weight = round(final_weight, 2)

    # Return the answer in pounds
    result = final_weight * 2.2
    return result

print(solution())