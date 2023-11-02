def solution():
    """Amanda had 10 notebooks. This week, she ordered 6 more and then lost 2. How many notebooks does Amanda have now?"""
    # Define the initial number of notebooks
    notebooks = 10

    # Add the notebooks she ordered
    notebooks += 6

    # Subtract the notebooks she lost
    notebooks -= 2

    # Return the current number of notebooks
    result = notebooks
    return result

print(solution())