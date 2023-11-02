def solution():
    leak_rate = 1.5
    hours_until_return = 12
    total_leakage = leak_rate * hours_until_return
    bucket_size = total_leakage * 2
    result = bucket_size
    return result

print(solution())