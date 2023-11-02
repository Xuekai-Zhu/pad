def solution():
    # Calculate the number of rounds needed to fill the pool
    george_buckets = 2
    harry_buckets = 3
    total_buckets = 110
    total_rounds = total_buckets // (george_buckets + harry_buckets)
    if total_buckets % (george_buckets + harry_buckets) != 0:
        total_rounds += 1
    result = total_rounds
    return result

print(solution())