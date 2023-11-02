def solution():
    """Billy buys a 12 pack of soda from the store. If he has twice as many brothers as sisters, and he has 2 sisters, how many sodas can he give to each of his siblings if he wants to give out the entire 12 pack while giving each the same number?"""
    sisters = 2
    brothers = 4
    siblings = sisters + brothers
    sodas_per_sibling = 12 // siblings
    result = sodas_per_sibling
    return result

print(solution())