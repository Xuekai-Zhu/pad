def solution():
    starting_weight = 97
    weight_loss_per_month = 3
    months_to_fight = 4

    # Calculate the total weight loss before the fight
    total_weight_loss = weight_loss_per_month * months_to_fight

    # Calculate the boxer's weight on the day of the fight
    weight_on_fight_day = starting_weight - total_weight_loss
    result = weight_on_fight_day
    return result

print(solution())