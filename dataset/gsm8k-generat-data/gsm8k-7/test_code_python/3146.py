def solution():
    george_buckets_per_round = 2
    harry_buckets_per_round = 3
    total_buckets = 110

    # Calculate the total number of rounds it will take to fill the pool
    total_rounds = (total_buckets // (george_buckets_per_round + harry_buckets_per_round)) + (1 if total_buckets % (george_buckets_per_round + harry_buckets_per_round) else 0)
    result = total_rounds
    return result

print(solution())