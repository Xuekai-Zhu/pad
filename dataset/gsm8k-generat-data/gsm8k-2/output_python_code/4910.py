def solution():
    """Ajax is 80 kilograms. He is planning to lose some weight. Exercising for an hour will help him lose 1.5 pounds. If 1 kilogram is equal to 2.2 pounds How many pounds will he weigh if he exercises for 2 hours every day for two weeks?"""
    ajax_weight = 80 * 2.2  # convert to pounds
    exercise_time = 2  # hours
    weight_loss_per_hour = 1.5
    total_weight_loss = (weight_loss_per_hour * exercise_time) * 14  # two weeks
    final_weight = ajax_weight - total_weight_loss
    result = final_weight
    return result

print(solution())