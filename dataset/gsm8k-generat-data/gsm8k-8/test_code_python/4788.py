def solution():
    pants_cost = 20
    shirt_cost = 2 * pants_cost
    tie_cost = shirt_cost / 5
    socks_cost = 3
    total_cost = 5 * (pants_cost + shirt_cost + tie_cost + 2 * socks_cost)
    result = total_cost
    return result

print(solution())