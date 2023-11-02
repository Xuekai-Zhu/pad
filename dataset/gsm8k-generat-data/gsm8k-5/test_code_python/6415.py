def solution():
    # Let x be the maximum number of people who can fit on the raft without life jackets
    # Then, x-7 is the maximum number of people who can fit on the raft with life jackets
    # And, 21-x is the number of people on the raft without life jackets
    # And, 8 is the number of people on the raft who need life jackets

    # Using these equations, we can set up the following equation to solve for x:
    x - 7 = 21 - x - 8
    # Simplifying and solving for x:
    2x = 42
    x = 21

    # Therefore, the maximum number of people who can fit on the raft without life jackets is 21.
    result = 21
    return result

print(solution())