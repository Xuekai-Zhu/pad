def solution():
    women = 0.5
    men = 0.5
    total = women + men
    in_favor = 0.35
    opposed = 0.39
    result = (in_favor * total) / opposed
    return result

print(solution())