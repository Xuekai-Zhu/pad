def solution():
    # Let x be the number of people who could fit on the raft without life jackets
    x = 21
    # Let y be the number of people who could fit on the raft with life jackets
    y = x - 7
    # Let z be the total number of people on the raft including those who need life jackets
    z = 21 + 8
    # Use the equation (x-8) + y = z to solve for y
    y = z - x + 8
    result = x + y
    return result

print(solution())