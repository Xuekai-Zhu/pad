def solution():
    """A colony of bees can contain up to 80000 individuals. In winter they are more exposed to death, and if the winter is really cold the bees can begin to die slowly. If the colony starts to lose 1200 bees per day, how many days will pass until the number of bees in the colony reaches a fourth of its initial number?"""
    initial_bees = 80000
    current_bees = initial_bees
    days = 0
    while current_bees > initial_bees / 4:
        current_bees -= 1200
        days += 1
    result = days
    return result

print(solution())