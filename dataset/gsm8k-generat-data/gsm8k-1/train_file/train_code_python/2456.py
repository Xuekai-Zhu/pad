def solution():
    """A colony of bees can contain up to 80000 individuals. In winter they are more exposed to death, and if the winter is really cold the bees can begin to die slowly. If the colony starts to lose 1200 bees per day, how many days will pass until the number of bees in the colony reaches a fourth of its initial number?"""
    initial_number = 80000
    fourth_number = initial_number / 4
    daily_loss = 1200
    days_to_reach_fourth = (initial_number - fourth_number) / daily_loss
    result = days_to_reach_fourth
    return result

print(solution())