def solution():
    """A boxer weighs 97 kg at 4 months from a fight. He is on a diet that allows him to lose 3 kg per month until the day of the fight. How much will he weigh on the day of the fight?"""
    initial_weight = 97
    weight_loss_per_month = 3
    months_until_fight = 4
    total_weight_loss = weight_loss_per_month * months_until_fight
    weight_on_fight_day = initial_weight - total_weight_loss
    result = weight_on_fight_day
    return result

print(solution())