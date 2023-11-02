def solution():
    """Collin learned that he could earn $0.25 per aluminum can that he brought into the recycling center. He found 12 cans at home and three times as many at his grandparents' house. His neighbor gave him 46. His dad brought home 250 cans from the office. His dad told him he could keep the money from the cans he brought home from the office if he promised to put half of his entire amount collected into savings. How much money would Collin have to put into savings?"""
    price_per_can = 0.25
    cans_at_home = 12
    cans_at_grandparents = 3*cans_at_home
    cans_from_neighbor = 46
    cans_from_dad = 250
    total_cans = cans_at_home + cans_at_grandparents + cans_from_neighbor + cans_from_dad
    total_money = total_cans * price_per_can
    savings = total_money/2
    result = savings
    return result

print(solution())