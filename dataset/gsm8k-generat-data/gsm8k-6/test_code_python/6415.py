def solution():
    # Calculate the number of people who can fit on the raft without life jackets
    no_jacket_capacity = 21

    # Calculate the number of people who can fit on the raft with life jackets
    jacket_capacity = no_jacket_capacity - 7

    # Calculate the total number of people who can fit on the raft
    total_capacity = jacket_capacity + 8  # 8 people need life jackets

    result = total_capacity
    return result

print(solution())