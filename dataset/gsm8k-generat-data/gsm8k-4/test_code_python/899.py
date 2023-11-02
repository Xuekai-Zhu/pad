def solution():
    """Ben works 8-hour shifts in a furniture shop. It takes him 5 hours to build 1 rocking chair. How many chairs can he build in 10 days?"""
    # Define the number of work hours in 10 days
    total_hours = 10 * 8

    # Calculate the number of chairs Ben can build in 10 days
    chairs_built = total_hours // 5

    result = chairs_built
    return result

print(solution())