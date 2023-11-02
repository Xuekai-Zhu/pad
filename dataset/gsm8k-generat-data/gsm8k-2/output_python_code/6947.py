def solution():
    """Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. How many cherry saplings does she have left?"""
    cherry_pits = 80
    sprout_percentage = 0.25
    sprouted_pits = cherry_pits * sprout_percentage
    remaining_saplings = sprouted_pits - 6
    result = remaining_saplings
    return result

print(solution())