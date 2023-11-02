def solution():
    goal = 50 * 7 # 7 days in a week
    total_read = 43 + 65 + 28 + 0 + 70 + 56 # pages read from Sunday to Friday
    pages_to_go = goal - total_read
    result = pages_to_go
    return result

print(solution())