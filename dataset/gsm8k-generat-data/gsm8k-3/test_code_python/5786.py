def solution():
    """Shelby was having a movie party for her birthday. She and her mom made a dozen bags of buttered popcorn and 10 bags of caramel popcorn. Her brother Alan took 3 bags of buttered popcorn and 1 bag of caramel popcorn for his friends. How many bags of popcorn does Shelby have left for the party?"""
    # Define the amount of popcorn bags 
    BUTTERED_POPCORN = 12
    CARAMEL_POPCORN = 10

    # Define the amount of popcorn bags Alan took
    ALAN_BUTTERED = 3
    ALAN_CARAMEL = 1

    # Calculate the remaining amount of popcorn bags for the party
    remaining_buttered = BUTTERED_POPCORN - ALAN_BUTTERED
    remaining_caramel = CARAMEL_POPCORN - ALAN_CARAMEL

    # Display the amount of popcorn bags remaining
    result = remaining_buttered + remaining_caramel
    return result

print(solution())