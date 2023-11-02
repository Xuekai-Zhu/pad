def solution():
    """Peter bought 4 new notebooks for school. 2 of them are green, one is black and the other one is pink. The total cost was $45. If the black notebook cost $15, and the pink one cost $10, how much did the green notebooks cost each?"""
    # Define the cost of the black and pink notebooks
    black_cost = 15
    pink_cost = 10

    # Calculate the total cost of the four notebooks
    total_cost = 45

    # Calculate the cost of the two green notebooks
    green_cost = (total_cost - black_cost - pink_cost) / 2

    # Display the cost of each green notebook
    result = green_cost / 2
    return result

print(solution())