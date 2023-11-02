def solution():
    """Kim plants 80 cherry pits. 25% of them sprout and Kim sells 6 of the saplings. How many cherry saplings does she have left?"""
    # Define the number of cherry pits planted and the percentage that sprouted
    pits_planted = 80
    sprout_percentage = 0.25

    # Calculate the number of cherry saplings that sprouted
    sprouted_saplings = pits_planted * sprout_percentage

    # Calculate the number of cherry saplings remaining after selling 6
    remaining_saplings = sprouted_saplings - 6

    # Display the number of cherry saplings remaining
    result = remaining_saplings
    return result

print(solution())