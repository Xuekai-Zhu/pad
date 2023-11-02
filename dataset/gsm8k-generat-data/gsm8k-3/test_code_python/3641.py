def solution():
    """Bobby wanted pancakes for breakfast.  The recipe on the box makes 21 pancakes.  While he ate 5 pancakes, his dog jumped up and was able to eat 7 before being caught.  How many pancakes does Bobby have left?"""
    # Define the number of pancakes in the recipe
    RECIPE_PANCAKES = 21

    # Calculate the number of pancakes Bobby has left
    pancakes_left = RECIPE_PANCAKES - 5 - 7

    # Display the number of pancakes Bobby has left
    result = pancakes_left
    return result

print(solution())