def solution():
    """Joan is preparing sandwiches for a family potluck. She decides to make ham sandwiches and grilled cheese sandwiches. One ham sandwich requires 2 slices of cheese, and one grilled cheese sandwich requires 3 slices of cheese. She uses a total of 50 slices of cheese to make the sandwiches. If she makes 10 ham sandwiches, how many grilled cheese sandwiches does she make?"""
    # Define the number of slices of cheese needed for a ham sandwich and for a grilled cheese sandwich
    ham_cheese = 2
    grilled_cheese = 3

    # Define the number of ham sandwiches made
    ham_sandwiches = 10

    # Calculate the number of slices of cheese used for the ham sandwiches
    ham_cheese_used = ham_sandwiches * ham_cheese

    # Calculate the remaining number of slices of cheese after making the ham sandwiches
    remaining_cheese = 50 - ham_cheese_used

    # Calculate the number of grilled cheese sandwiches that can be made with the remaining cheese
    grilled_cheese_sandwiches = remaining_cheese // grilled_cheese

    # Return the result
    result = grilled_cheese_sandwiches
    return result

print(solution())