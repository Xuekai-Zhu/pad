def solution():
    leak_rate = 1.5  # The fish tank leaks at a rate of 1.5 ounces per hour
    max_leak = 12 * leak_rate  # The maximum amount that could leak over 12 hours
    bucket_size = 2 * max_leak  # The bucket can hold twice the max amount that could leak
    result = bucket_size
    return result

print(solution())