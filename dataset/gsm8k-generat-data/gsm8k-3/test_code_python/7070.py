def solution():
    """Two pieces of bread are needed for one regular sandwich. 3 pieces of bread are needed for a double meat sandwich. How many pieces of bread are needed for 14 regular sandwiches and 12 double meat sandwiches?"""
    # Define the number of pieces of bread needed for each type of sandwich
    REGULAR_BREAD = 2
    DOUBLE_BREAD = 3

    # Define the number of each type of sandwich
    num_regular = 14
    num_double = 12

    # Calculate the total number of pieces of bread needed
    total_bread = (num_regular * REGULAR_BREAD) + (num_double * DOUBLE_BREAD)

    # Display the total number of pieces of bread needed
    result = total_bread
    return result

print(solution())