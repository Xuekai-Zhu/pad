def solution():
    starting_balls = 175
    first_100_hits = int(2/5 * 100)
    next_75_hits = int(1/3 * 75)

    total_hits = first_100_hits + next_75_hits

    not_hit = starting_balls - total_hits
    result = not_hit
    return result

print(solution())