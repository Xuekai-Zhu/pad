def solution():
    """James catches 3 kinds of fish. He catches 200 pounds of trout, 50% more pounds of salmon, and twice as much tuna. How many pounds of fish did he catch?"""
    # Calculate the number of pounds of salmon caught
    salmon_pounds = 200 * 1.5

    # Calculate the number of pounds of tuna caught
    tuna_pounds = 200 * 2

    # Calculate the total number of pounds of fish caught
    total_pounds = 200 + salmon_pounds + tuna_pounds

    # Return the result
    result = total_pounds
    return result

print(solution())