def solution():
    simon_sticks = 36
    gerry_sticks = (2/3) * simon_sticks
    simon_gerry_sticks = simon_sticks + gerry_sticks
    micky_sticks = simon_gerry_sticks + 9

    total_sticks = simon_sticks + gerry_sticks + micky_sticks
    result = total_sticks
    return result

print(solution())