def solution():
    """Anna's mom gave her $10.00 to buy anything she wanted from the candy store. Anna bought 3 packs of chewing gum for $1.00 each, 5 chocolate bars at $1 each and 2 large candy canes for $0.50 each. How much money did Anna have left?"""
    total_cost = (3*1) + (5*1) + (2*0.5)
    money_left = 10 - total_cost
    result = money_left
    return result

print(solution())