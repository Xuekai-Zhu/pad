def solution():
    """Daliah picked up 17.5 pounds of garbage. Dewei picked up 2 pounds less than Daliah. Zane picked up 4 times as many pounds of garbage as Dewei. How many pounds of garbage did Zane pick up?"""
    daliah_garbage = 17.5
    dewei_garbage = daliah_garbage - 2
    zane_garbage = 4 * dewei_garbage
    result = zane_garbage
    return result

print(solution())