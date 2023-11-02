def solution():
    """Bobby wanted pancakes for breakfast. The recipe on the box makes 21 pancakes. While he ate 5 pancakes, his dog jumped up and was able to eat 7 before being caught. How many pancakes does Bobby have left?"""
    # Define the number of pancakes in the recipe
    pancakes_recipe = 21

    # Calculate the number of pancakes Bobby has left after eating and his dog eating
    pancakes_left = pancakes_recipe - 5 - 7

    # return the result
    result = pancakes_left
    return result

print(solution())