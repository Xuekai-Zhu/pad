def solution():
    """Cordelia is dyeing her hair red. To get the color she wants, she first has to bleach her dark brown hair to blonde, and then she has to apply the dye. The whole process will take 9 hours. Dyeing takes twice as long as bleaching. How many hours will it take Cordelia to bleach her hair?"""
    # Define the total time for both processes
    total_time = 9

    # Define the time for dyeing as twice the time for bleaching
    dyeing_time = 2 * bleaching_time

    # Calculate the time for bleaching
    bleaching_time = (total_time - dyeing_time) / 3

    result = bleaching_time
    return result

print(solution())