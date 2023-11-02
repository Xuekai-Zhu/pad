def solution():
    total_peaches = 250  # Brenda picks 250 peaches
    fresh_peaches = int(total_peaches * 0.6)  # 60% of the peaches are fresh
    fresh_peaches -= 15  # Brenda throws away 15 of the fresh peaches for being too small
    result = fresh_peaches
    return result

print(solution())