def solution():
    sock_weight = 2
    underwear_weight = 4
    shirt_weight = 5
    shorts_weight = 8
    pants_weight = 10
    total_weight = 2 * sock_weight + 2 * underwear_weight + 2 * shirt_weight + shorts_weight + pants_weight
    max_weight = 50
    result = max_weight - total_weight
    return result

print(solution())