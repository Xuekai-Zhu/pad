def solution():
    """Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"""
    # Define the initial number of tadpoles caught
    initial_tadpoles = 180

    # Calculate the number of tadpoles let go
    let_go = initial_tadpoles * 0.75

    # Calculate the number of tadpoles kept
    kept = initial_tadpoles - let_go

    # Display the number of tadpoles kept
    result = kept
    return result

print(solution())