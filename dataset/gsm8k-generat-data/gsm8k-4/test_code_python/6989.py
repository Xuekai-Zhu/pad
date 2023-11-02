def solution():
    """An artist spends 30 hours every week painting. If it takes her 3 hours to complete a painting, how many paintings can she make in four weeks?"""
    # Define the number of hours the artist spends painting in 4 weeks
    total_hours = 30 * 4

    # Calculate the number of paintings she can complete in 4 weeks
    num_paintings = total_hours // 3

    # return the result
    result = num_paintings
    return result

print(solution())