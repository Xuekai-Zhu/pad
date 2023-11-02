def solution():
    """Randy had 32 biscuits. His father gave him 13 biscuits as a gift. His mother gave him 15 biscuits. Randy’s brother ate 20 of these biscuits. How many biscuits are Randy left with?"""
    initial_biscuits = 32
    father_biscuits = 13
    mother_biscuits = 15
    brother_biscuits = 20
    total_biscuits = initial_biscuits + father_biscuits + mother_biscuits - brother_biscuits
    result = total_biscuits
    return result

print(solution())