def solution():
    """Simon, Gerry, and Micky want to have a race with handmade miniature rafts. Simon's raft needs 36 sticks, Gerry's raft needs two-thirds of the number of sticks that Simon needs, and Micky's raft needs 9 sticks more than Simon and Gerry's rafts combined. How many sticks do the three boys need to collect in total?"""
    simon_sticks = 36
    gerry_sticks = (2/3) * simon_sticks
    combined_sticks = simon_sticks + gerry_sticks
    micky_sticks = combined_sticks + 9
    total_sticks = simon_sticks + gerry_sticks + micky_sticks
    result = total_sticks
    return result

print(solution())