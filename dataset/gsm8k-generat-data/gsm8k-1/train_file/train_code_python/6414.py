def solution():
    """There was only enough room for 21 people on a raft if no one wore life jackets. There were 7 fewer people who could fit on the raft if everyone wore life jackets. If 8 people on the raft needed life jackets, how many people could fit on the raft?"""
    no_jackets_capacity = 21
    jacket_capacity = no_jackets_capacity - 7
    jackets_needed = 8
    total_capacity = no_jackets_capacity + (jacket_capacity * jackets_needed)
    result = total_capacity
    return result

print(solution())