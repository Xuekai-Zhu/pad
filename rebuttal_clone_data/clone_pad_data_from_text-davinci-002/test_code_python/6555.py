def solution():
    goal = 100 * 1.2
    days = 280
    week = days / 7
    increase = (goal - 100) / week
    result = increase
    return result

print(solution())