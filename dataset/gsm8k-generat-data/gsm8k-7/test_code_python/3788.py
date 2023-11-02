def solution():
    total_fish = 15 + (15 * 3)  # 15 on day 1 and 3 times as many on day 2
    num_sharks = total_fish * 0.25  # 25% of the fish are sharks
    result = num_sharks
    return result

print(solution())