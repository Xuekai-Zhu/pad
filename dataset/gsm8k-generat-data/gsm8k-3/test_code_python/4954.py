def solution():
    """Jangshe spent $610 on 7 pieces of clothing. One piece was $49 and another piece was $81. If the other pieces were all the same price, how many dollars was one of the other pieces?"""
    # Define the total amount spent
    total_spent = 610

    # Define the prices of the known pieces of clothing
    piece1 = 49
    piece2 = 81

    # Calculate the total cost of the known pieces
    known_cost = piece1 + piece2

    # Calculate the number of unknown pieces
    unknown_count = 7 - 2

    # Calculate the cost of each unknown piece
    unknown_cost = (total_spent - known_cost) / unknown_count

    # Display the cost of each unknown piece
    result = unknown_cost
    return result

print(solution())