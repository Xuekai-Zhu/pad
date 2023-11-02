def solution():
    # Calculate the number of pancakes Bobby has left
    total_pancakes = 21  # number of pancakes in the recipe
    eaten_pancakes = 5 + 7  # pancakes eaten by Bobby and his dog
    remaining_pancakes = total_pancakes - eaten_pancakes  # pancakes left
    result = remaining_pancakes
    return result

print(solution())