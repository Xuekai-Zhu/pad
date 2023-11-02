def solution():
    """Simon, Gerry, and Micky want to have a race with handmade miniature rafts. Simon's raft needs 36 sticks, Gerry's raft needs two-thirds of the number of sticks that Simon needs, and Micky's raft needs 9 sticks more than Simon and Gerry's rafts combined. How many sticks do the three boys need to collect in total?"""
    # Define the number of sticks needed for Simon's raft
    simon_sticks = 36

    # Define the number of sticks needed for Gerry's raft in terms of the number of sticks needed for Simon's raft
    gerry_sticks = (2/3) * simon_sticks

    # Define the total number of sticks needed for Simon and Gerry's rafts combined
    simon_gerry_sticks = simon_sticks + gerry_sticks

    # Define the number of sticks needed for Micky's raft in terms of the number of sticks needed for Simon and Gerry's rafts combined
    micky_sticks = simon_gerry_sticks + 9

    # Calculate the total number of sticks needed for all three rafts
    total_sticks = simon_sticks + gerry_sticks + micky_sticks

    # return the result
    result = total_sticks
    return result

print(solution())