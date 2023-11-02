def solution():
    """A boxer weighs 97 kg at 4 months from a fight. He is on a diet that allows him to lose 3 kg per month until the day of the fight. How much will he weigh on the day of the fight?"""
    # Define the initial weight and the weight loss per month
    initial_weight = 97
    weight_loss_per_month = 3

    # Calculate the weight on the day of the fight
    weight_on_fight_day = initial_weight - (weight_loss_per_month * 4)

    result = weight_on_fight_day
    return result

print(solution())