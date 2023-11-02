def solution():
    """Randy had 32 biscuits. His father gave him 13 biscuits as a gift. His mother gave him 15 biscuits. Randy’s brother ate 20 of these biscuits. How many biscuits are Randy left with?"""
    initial_biscuits = 32
    father_gift = 13
    mother_gift = 15
    brother_eaten = 20
    total_biscuits = initial_biscuits + father_gift + mother_gift - brother_eaten
    result = total_biscuits
    return result

print(solution())