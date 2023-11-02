def solution():
    total_seeds_collected = 4*6 + 3*2 + 9*3 # calculate total seeds collected
    seeds_needed = 60 - total_seeds_collected # calculate remaining seeds needed
    result = seeds_needed
    return result

print(solution())