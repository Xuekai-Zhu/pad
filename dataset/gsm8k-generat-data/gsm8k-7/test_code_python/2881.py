def solution():
    num_fish = 50
    num_tadpoles = 3 * num_fish

    # Remove 7 fish from the pond
    num_fish -= 7

    # Half of the remaining tadpoles will develop into frogs
    num_tadpoles /= 2

    # Calculate the difference between the number of tadpoles and fish
    difference = num_tadpoles - num_fish
    result = difference
    return result

print(solution())