def solution():
    """Nathan plays amateur baseball. He played for 3 hours for two weeks, every day. His friend Tobias played for 5 hours every day, but only for one week. How many hours did Nathan and Tobias play in total?"""
    # Calculate Nathan's total playing time
    nathan_time = 3 * 7 * 2

    # Calculate Tobias's total playing time
    tobias_time = 5 * 7 * 1

    # Calculate the total playing time for Nathan and Tobias
    total_time = nathan_time + tobias_time

    # Return the result
    result = total_time
    return result

print(solution())