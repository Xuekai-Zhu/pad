def solution():
    num_misses = 50
    num_hits = num_misses / 3
    total = num_misses + num_hits
    result = {"misses": num_misses, "hits": num_hits, "total": total}
    return result

print(solution())