def solution():
    
    george_buckets = 2
    harry_buckets = 3
    total_buckets = 110
    rounds = (total_buckets - 1) // (george_buckets + harry_buckets) + 1
    result = rounds
    return result

print(solution())