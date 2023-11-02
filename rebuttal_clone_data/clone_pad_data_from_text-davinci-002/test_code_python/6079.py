def solution():
    total_curlers = 16
    small_pink_curlers = total_curlers / 4
    medium_blue_curlers = small_pink_curlers * 2
    large_green_curlers = total_curlers - small_pink_curlers - medium_blue_curlers
    result = large_green_curlers
    return result

print(solution())