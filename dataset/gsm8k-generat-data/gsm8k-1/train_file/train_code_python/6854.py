def solution():
    """Cordelia is dyeing her hair red. To get the color she wants, she first has to bleach her dark brown hair to blonde, and then she has to apply the dye. The whole process will take 9 hours. Dyeing takes twice as long as bleaching. How many hours will it take Cordelia to bleach her hair?"""
    total_time = 9
    bleach_time = total_time / 3
    dye_time = bleach_time * 2
    result = bleach_time
    return result

print(solution())