def solution():
    george_buckets = 2
    harry_buckets = 3
    total_buckets = 110

    # Calculate the total number of rounds required to fill the pool
    total_rounds = (total_buckets / (george_buckets + harry_buckets))
    result = total_rounds
    return result

print(solution())