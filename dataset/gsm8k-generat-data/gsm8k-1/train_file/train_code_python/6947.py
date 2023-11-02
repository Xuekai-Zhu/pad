def solution():
    """Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. How many cherry saplings does she have left?"""
    cherry_pits = 80
    sprout_percentage = 0.25
    sprouted_pits = cherry_pits * sprout_percentage
    saplings_sold = 6
    saplings_left = sprouted_pits - saplings_sold
    result = saplings_left
    return result

print(solution())