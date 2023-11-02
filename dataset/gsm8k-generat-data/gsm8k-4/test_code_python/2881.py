def solution():
    """There were 50 fish in a pond and 3 times as many tadpoles.
    If Curtis catches 7 fish and half the tadpoles develop into frogs,
    how many more tadpoles than fish are there in the pond now?"""
    # Define the initial number of fish and tadpoles
    fish = 50
    tadpoles = fish * 3

    # Catch 7 fish
    fish -= 7

    # Half of the tadpoles develop into frogs
    tadpoles /= 2

    # Calculate the difference between the number of tadpoles and fish
    difference = tadpoles - fish

    # Return the result
    result = difference
    return result

print(solution())