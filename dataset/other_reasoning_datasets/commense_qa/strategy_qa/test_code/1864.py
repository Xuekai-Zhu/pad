def solution():
    max_diving_depth = 60
    giant_squid_depth_range = [1000, 3800]
    if max(giant_squid_depth_range) > max_diving_depth:
        result = "impossible without gear"
    else:
        result = "possible without gear"
    return result

print(solution())