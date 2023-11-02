def solution():
    # Calculate the total number of buckets of fish consumed by all the sea animals
    total_buckets = 4 + 2 + 20  # dolphins are fed half as many buckets as sharks (2), other sea animals are fed 5 times as many buckets as sharks (20)

    # Calculate the number of weeks 546 buckets of fish will last
    weeks = 546 // total_buckets  # // is used for integer division
    result = weeks
    return result

print(solution())