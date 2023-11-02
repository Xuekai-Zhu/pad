def solution():
    """Ajax is 80 kilograms. He is planning to lose some weight. Exercising for an hour will help him lose 1.5 pounds. If 1 kilogram is equal to 2.2 pounds, how many pounds will he weigh if he exercises for 2 hours every day for two weeks?"""
    ajax_weight_kg = 80
    exercise_time = 2 # hours
    weight_loss_per_hour = 1.5 # pounds
    conversion_factor = 2.2 # pounds per kilogram
    exercise_days = 14 # two weeks
    total_exercise_time = exercise_time * exercise_days
    total_weight_loss = weight_loss_per_hour * total_exercise_time
    total_weight_loss_kg = total_weight_loss / conversion_factor
    ajax_weight_pounds = ajax_weight_kg * conversion_factor
    final_weight_pounds = ajax_weight_pounds - total_weight_loss_kg
    result = final_weight_pounds
    return result

print(solution())