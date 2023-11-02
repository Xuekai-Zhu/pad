def solution():
    """A boxer weighs 97 kg at 4 months from a fight. He is on a diet that allows him to lose 3 kg per month until the day of the fight. How much will he weigh on the day of the fight?"""
    # Define the initial weight of the boxer
    initial_weight = 97

    # Define the weight loss per month
    weight_loss_per_month = 3

    # Define the number of months until the fight
    months_until_fight = 4

    # Calculate the weight of the boxer on the day of the fight
    final_weight = initial_weight - (weight_loss_per_month * months_until_fight)

    # return the result
    result = final_weight
    return result

print(solution())