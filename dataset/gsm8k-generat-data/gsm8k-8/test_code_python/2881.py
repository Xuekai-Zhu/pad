def solution():
    # Define the initial number of fish and tadpoles
    fish_count = 50
    tadpole_count = 3 * fish_count

    # Remove 7 fish from the pond
    fish_count -= 7

    # Calculate the number of tadpoles that develop into frogs
    tadpoles_to_frogs = 0.5 * tadpole_count
    tadpole_count -= tadpoles_to_frogs

    # Calculate the difference between the number of tadpoles and fish
    diff = tadpole_count - fish_count
    result = diff
    return result

print(solution())