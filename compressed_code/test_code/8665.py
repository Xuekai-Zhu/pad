def solution():
    
    starting_pancakes = 21
    pancakes_eaten = 5
    pancakes_stolen_by_dog = 7
    pancakes_left = starting_pancakes - pancakes_eaten - pancakes_stolen_by_dog
    result = pancakes_left
    return result

print(solution())