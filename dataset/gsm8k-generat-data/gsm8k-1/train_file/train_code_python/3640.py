def solution():
    """Bobby wanted pancakes for breakfast. The recipe on the box makes 21 pancakes. While he ate 5 pancakes, his dog jumped up and was able to eat 7 before being caught. How many pancakes does Bobby have left?"""
    starting_pancakes = 21
    pancakes_eaten = 5
    pancakes_stolen_by_dog = 7
    pancakes_left = starting_pancakes - pancakes_eaten - pancakes_stolen_by_dog
    result = pancakes_left
    return result

print(solution())