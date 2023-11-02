def solution():
    recipe = 21
    eaten_by_bobby = 5
    eaten_by_dog = 7

    # Calculate the total number of pancakes left
    remaining_pancakes = recipe - eaten_by_bobby - eaten_by_dog
    result = remaining_pancakes
    return result

print(solution())