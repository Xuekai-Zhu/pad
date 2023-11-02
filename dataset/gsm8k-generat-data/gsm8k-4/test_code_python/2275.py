def solution():
    """Mary bought six apples from the store. From the apples she bought, for each that Mary ate, she planted two trees from the remaining ones. How many apples did Mary eat?"""
    # Define the initial number of apples
    initial_apples = 6

    # Initialize the number of apples that Mary ate and the number of remaining apples
    ate_apples = 0
    remaining_apples = initial_apples

    # Calculate the number of apples that Mary ate and planted trees
    while remaining_apples >= 1:
        # Eat one apple
        ate_apples += 1
        remaining_apples -= 1

        # Plant two trees from the remaining apples
        planted_trees = remaining_apples * 2
        remaining_apples += planted_trees

    # return the result (the number of apples that Mary ate)
    result = ate_apples
    return result

print(solution())