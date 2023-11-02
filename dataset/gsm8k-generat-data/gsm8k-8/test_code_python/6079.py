def solution():
    total_curlers = 16
    pink_curlers = total_curlers / 4
    blue_curlers = 2 * pink_curlers
    green_curlers = total_curlers - pink_curlers - blue_curlers
    result = green_curlers
    return result

print(solution())