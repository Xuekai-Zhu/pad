def solution():
    """Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. How many cherry saplings does she have left?"""
    # Define the initial number of cherry pits
    cherry_pits = 80

    # Calculate the number of sprouted pits
    sprouted_pits = cherry_pits * 0.25

    # Calculate the number of saplings left after selling 6
    remaining_saplings = sprouted_pits - 6

    # return the result
    result = remaining_saplings
    return result

print(solution())