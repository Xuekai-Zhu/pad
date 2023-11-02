def solution():
    # Define the starting weight and weight loss per month
    starting_weight = 97
    weight_loss_per_month = 3

    # Calculate the weight on the day of the fight
    months_until_fight = 4 # given
    weight_on_fight_day = starting_weight - (weight_loss_per_month * months_until_fight)

    result = weight_on_fight_day
    return result

print(solution())