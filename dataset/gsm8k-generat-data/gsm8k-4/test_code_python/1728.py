def solution():
    """Jana is 5 inches taller than Kelly, and Kelly is 3 inches shorter than Jess. If Jess is 72 inches tall, how tall is Jana?"""
    # Define Jess's height
    jess_height = 72

    # Calculate Kelly's height
    kelly_height = jess_height - 3

    # Calculate Jana's height
    jana_height = kelly_height + 5

    # return the result
    result = jana_height
    return result

print(solution())