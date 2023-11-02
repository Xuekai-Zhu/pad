def solution():
    """Emily has 7 times as many oranges as Sandra. Sandra has 3 times as many oranges as Betty. If Betty has 12 oranges, how many oranges does Emily have?"""
    # Define the number of oranges Betty has
    betty_oranges = 12

    # Calculate the number of oranges Sandra has
    sandra_oranges = betty_oranges * 3

    # Calculate the number of oranges Emily has
    emily_oranges = sandra_oranges * 7

    # Return the result
    result = emily_oranges
    return result

print(solution())