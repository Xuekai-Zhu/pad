def solution():
    # Calculate the length of the path without the bridge
    path_length = 900 - 42

    # Calculate the number of fence poles needed for one side of the path
    poles_per_side = path_length // 6

    # Calculate the total number of fence poles needed for both sides of the path
    total_poles = poles_per_side * 2

    result = total_poles
    return result

print(solution())