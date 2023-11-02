def solution():
    autumn_months = ["September", "October", "November", "December"]
    bloom_time = "spring"
    if bloom_time not in autumn_months:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())