def solution():
    """A boxer weighs 97 kg at 4 months from a fight. He is on a diet that allows him to lose 3 kg per month until the day of the fight. How much will he weigh on the day of the fight?"""
    starting_weight = 97
    weight_loss_per_month = 3
    target_month = 0
    target_weight = 0
    for i in range(1, 5):
        current_month_weight = starting_weight - (weight_loss_per_month * i)
        if current_month_weight <= 0:
            target_month = i
            target_weight = current_month_weight
            break

    final_weight = starting_weight - (weight_loss_per_month * target_month)
    result = final_weight
    return result

print(solution())