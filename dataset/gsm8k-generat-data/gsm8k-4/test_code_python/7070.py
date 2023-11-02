def solution():
    """Two pieces of bread are needed for one regular sandwich. 3 pieces of bread are needed for a double meat sandwich. How many pieces of bread are needed for 14 regular sandwiches and 12 double meat sandwiches?"""
    # Define the number of pieces of bread needed per regular sandwich and per double meat sandwich
    REGULAR_SANDWICH_BREAD = 2
    DOUBLE_MEAT_SANDWICH_BREAD = 3

    # Calculate the total number of pieces of bread needed for 14 regular sandwiches
    num_regular_sandwiches = 14
    total_regular_sandwich_bread = num_regular_sandwiches * REGULAR_SANDWICH_BREAD

    # Calculate the total number of pieces of bread needed for 12 double meat sandwiches
    num_double_meat_sandwiches = 12
    total_double_meat_sandwich_bread = num_double_meat_sandwiches * DOUBLE_MEAT_SANDWICH_BREAD

    # Calculate the total number of pieces of bread needed
    total_bread = total_regular_sandwich_bread + total_double_meat_sandwich_bread

    result = total_bread
    return result

print(solution())