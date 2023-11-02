def solution():
    # Calculate the total number of cucumber and egg sandwiches
    cucumber_sandwiches = 10
    egg_sandwiches = 8

    # Calculate the total number of bread slices
    cucumber_slices = 4 * cucumber_sandwiches
    egg_slices = 2 * egg_sandwiches
    total_slices = cucumber_slices + egg_slices

    # Calculate the number of bread slices eaten by the guests
    eaten_slices = 28 + 12

    # Calculate the remaining number of bread slices
    remaining_slices = total_slices - eaten_slices
    result = remaining_slices
    return result

print(solution())