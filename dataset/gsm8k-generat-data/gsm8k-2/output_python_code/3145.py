def solution():
    """George and Harry want to fill a pool with buckets. George can carry two buckets each round, and Harry can carry three buckets each round. If it takes 110 buckets to fill the pool, how many rounds will it take to fill the pool?"""
    george_buckets = 2
    harry_buckets = 3
    total_buckets = 110
    rounds = (total_buckets - 1) // (george_buckets + harry_buckets) + 1
    result = rounds
    return result

print(solution())