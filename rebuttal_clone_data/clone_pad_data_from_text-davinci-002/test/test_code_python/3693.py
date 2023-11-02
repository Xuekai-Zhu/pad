def solution():
    flat_rate = 20
    per_minute = 7
    total_paid = 146
    minutes = (total_paid - flat_rate) / per_minute
    result = minutes
    return result

print(solution())