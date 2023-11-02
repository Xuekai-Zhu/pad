def solution():
    """The first store charges $3 for 6 apples while the second store charges $4 for 10 apples. How many cents can you save on each apple from buying $4 for 10 apples than from $3 for 6 apples?"""
    # Calculate the cost per apple from the first store
    store1_cost_per_apple = 3/6

    # Calculate the cost per apple from the second store
    store2_cost_per_apple = 4/10

    # Calculate the difference in cost per apple
    cost_difference = store1_cost_per_apple - store2_cost_per_apple

    # Convert the cost difference to cents
    cents_saved = cost_difference * 100

    # Display the result
    result = cents_saved
    return result

print(solution())