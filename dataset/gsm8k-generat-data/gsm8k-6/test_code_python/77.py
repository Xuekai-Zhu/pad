def solution():
    # Calculate the weight of the boxer on the day of the fight
    weight_loss = 3 * 5  # the boxer loses 3 kg per month for 5 months (from 4 months before the fight to the day of the fight)
    weight_fight = 97 - weight_loss
    result = weight_fight
    return result

print(solution())