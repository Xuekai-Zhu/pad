def solution():
    """John has a sneezing fit for 2 minutes. He sneezes once every 3 seconds. How many times does he sneeze?"""
    # Define the duration of John's sneezing fit in seconds
    duration = 2 * 60

    # Calculate the number of times John sneezes
    sneezes = duration // 3

    # return the result
    result = sneezes
    return result

print(solution())