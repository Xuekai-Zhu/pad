def solution():
    """Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"""
    # Define the initial number of tadpoles
    initial_tadpoles = 180

    # Calculate the number of tadpoles he let go
    released_tadpoles = initial_tadpoles * 0.75

    # Calculate the number of tadpoles he kept
    kept_tadpoles = initial_tadpoles - released_tadpoles

    # return the result
    result = kept_tadpoles
    return result

print(solution())