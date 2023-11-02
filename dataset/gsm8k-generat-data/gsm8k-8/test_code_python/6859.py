def solution():
    # Define the number of sticks that Simon's raft needs
    simon_sticks = 36

    # Define the number of sticks that Gerry's raft needs
    gerry_sticks = (2/3) * simon_sticks

    # Define the number of sticks that Micky's raft needs
    micky_sticks = simon_sticks + gerry_sticks + 9

    # Calculate the total number of sticks needed
    total_sticks = simon_sticks + gerry_sticks + micky_sticks
    result = total_sticks
    return result

print(solution())