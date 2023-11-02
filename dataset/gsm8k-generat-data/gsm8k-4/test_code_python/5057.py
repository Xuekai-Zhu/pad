def solution():
    """There are 21 cherry tomatoes on the tomato plant.  2 birds eat one-third of the tomatoes.  How many are still left on the tomato plant?"""
    # Define the initial number of tomatoes
    initial_tomatoes = 21

    # Calculate the number of tomatoes eaten by the birds
    bird_tomatoes = (1/3) * 2 #two birds are eating

    # Calculate the remaining number of tomatoes
    remaining_tomatoes = initial_tomatoes - bird_tomatoes

    # return the result
    result = remaining_tomatoes
    return result

print(solution())