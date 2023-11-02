def solution():
    """John has a sneezing fit for 2 minutes.  He sneezes once every 3 seconds.  How many times does he sneeze?"""
    # Convert time to seconds
    seconds = 2 * 60

    # Calculate the number of times John sneezes
    sneezes = seconds // 3

    # Display the number of times John sneezes
    result = sneezes
    return result

print(solution())