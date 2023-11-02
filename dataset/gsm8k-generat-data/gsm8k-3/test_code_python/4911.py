def solution():
    """Ajax is 80 kilograms. He is planning to lose some weight. Exercising for an hour will help him lose 1.5 pounds. If 1 kilogram is equal to 2.2 pounds How many pounds will he weigh if he exercises for 2 hours every day for two weeks?"""
    # Convert Ajax's weight from kilograms to pounds
    ajax_weight = 80 * 2.2 # 1 kilogram = 2.2 pounds

    # Calculate the number of hours Ajax will exercise in two weeks
    hours_exercised = 2 * 7 * 2 # 2 hours per day, 7 days per week, 2 weeks

    # Calculate the total weight Ajax will lose
    total_weight_lost = hours_exercised * 1.5 # 1.5 pounds lost per hour of exercise

    # Calculate Ajax's new weight in pounds
    new_weight = ajax_weight - total_weight_lost

    # Display Ajax's new weight in pounds
    result = new_weight
    return result

print(solution())