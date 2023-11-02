def solution():
    """Mary bought six apples from the store. From the apples she bought, for each that Mary ate, she planted two trees from the remaining ones. How many apples did Mary eat?"""
    # Define the number of apples that Mary bought
    total_apples = 6

    # Initialize the number of trees planted and apples eaten
    trees_planted = 0
    apples_eaten = 0

    # Loop through all the apples
    for i in range(total_apples):
        # If Mary eats an apple, increment the number of apples eaten
        if i % 2 == 0:
            apples_eaten += 1
        else:
            # Otherwise, plant two trees and decrement the number of remaining apples
            trees_planted += 2

    # Display the number of apples eaten
    result = apples_eaten
    return result

print(solution())