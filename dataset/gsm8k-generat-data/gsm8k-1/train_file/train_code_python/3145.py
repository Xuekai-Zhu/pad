def solution():
    """George and Harry want to fill a pool with buckets. George can carry two buckets each round, and Harry can carry three buckets each round. If it takes 110 buckets to fill the pool, how many rounds will it take to fill the pool?"""
    george_buckets_per_round = 2
    harry_buckets_per_round = 3
    total_buckets = 110
    rounds_needed = (total_buckets // (george_buckets_per_round + harry_buckets_per_round)) + 1
    result = rounds_needed
    return result

print(solution())