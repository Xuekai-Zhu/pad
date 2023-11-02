def solution():
    simon_sticks = 36
    gerry_sticks = simon_sticks / 3 * 2
    micky_sticks = simon_sticks + gerry_sticks + 9
    total_sticks = simon_sticks + gerry_sticks + micky_sticks
    
    return total_sticks

print(solution())