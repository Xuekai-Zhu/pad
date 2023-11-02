def solution():
    """Joan is preparing sandwiches for a family potluck. She decides to make ham sandwiches and grilled cheese sandwiches.
    One ham sandwich requires 2 slices of cheese, and one grilled cheese sandwich requires 3 slices of cheese.
    She uses a total of 50 slices of cheese to make the sandwiches. If she makes 10 ham sandwiches, how many grilled cheese sandwiches does she make?"""
    
    # Define the number of slices of cheese per ham sandwich and per grilled cheese sandwich
    CHEESE_PER_HAM = 2
    CHEESE_PER_GRILLED = 3

    # Define the number of ham sandwiches made
    ham_sandwiches = 10

    # Calculate the total number of slices of cheese used for the ham sandwiches
    cheese_for_ham = ham_sandwiches * CHEESE_PER_HAM

    # Calculate the remaining number of slices of cheese available for grilled cheese sandwiches
    cheese_for_grilled = 50 - cheese_for_ham

    # Calculate the number of grilled cheese sandwiches that can be made with the remaining cheese
    num_grilled = cheese_for_grilled // CHEESE_PER_GRILLED

    # Display the number of grilled cheese sandwiches that can be made
    result = num_grilled
    return result

print(solution())