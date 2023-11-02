def solution():
    """Shelby was having a movie party for her birthday. She and her mom made a dozen bags of buttered popcorn and 10 bags of caramel popcorn. Her brother Alan took 3 bags of buttered popcorn and 1 bag of caramel popcorn for his friends. How many bags of popcorn does Shelby have left for the party?"""
    # Define the initial number of bags of popcorn
    buttered_popcorn = 12
    caramel_popcorn = 10

    # Define the number of bags Alan took
    alan_buttered = 3
    alan_caramel = 1

    # Calculate the number of bags left for Shelby's party
    left_buttered = buttered_popcorn - alan_buttered
    left_caramel = caramel_popcorn - alan_caramel

    # Combine the remaining bags of popcorn
    total_left = left_buttered + left_caramel

    # return the result
    result = total_left
    return result

print(solution())