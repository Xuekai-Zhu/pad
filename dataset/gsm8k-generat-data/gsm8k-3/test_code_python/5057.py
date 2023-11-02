def solution():
    """There are 21 cherry tomatoes on the tomato plant.  2 birds eat one-third of the tomatoes.  How many are still left on the tomato plant?"""
    # Define the initial number of tomatoes
    tomatoes = 21

    # Calculate the number of tomatoes eaten by the birds
    birds_eaten = 2 * (1/3) * tomatoes

    # Calculate the remaining number of tomatoes
    remaining_tomatoes = tomatoes - birds_eaten

    # Display the number of remaining tomatoes
    result = remaining_tomatoes
    return result

print(solution())