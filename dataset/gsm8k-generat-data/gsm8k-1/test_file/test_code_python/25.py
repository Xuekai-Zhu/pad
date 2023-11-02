def solution():
    """Gloria is shoe shopping when she comes across a pair of boots that fit her shoe budget. However, she has to choose between the boots and two pairs of high heels that together cost five dollars less than the boots. If one pair of heels costs $33 and the other costs twice as much, how many dollars are the boots?"""
    heels1 = 33
    heels2 = heels1 * 2
    heels_total = heels1 + heels2
    boots = heels_total - 5
    result = boots
    return result

print(solution())