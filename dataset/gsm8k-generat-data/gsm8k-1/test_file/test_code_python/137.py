def solution():
    """There are 700 bees in a hive. There are twice as many worker bees as baby bees, and there are twice as many babies as queens. How many worker bees are there?"""
    total_bees = 700
    queens = total_bees // 6
    babies = queens * 2
    workers = babies * 2
    result = workers
    return result

print(solution())