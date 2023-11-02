def solution():
    starting_weight = 97  # The boxer weighs 97 kg four months from the fight
    monthly_weight_loss = 3  # The boxer loses 3 kg per month on his diet
    months_to_fight = 4  # The fight is in four months

    # Calculate the weight the boxer will be on the day of the fight
    final_weight = starting_weight - (monthly_weight_loss * months_to_fight)
    result = final_weight
    return result

print(solution())