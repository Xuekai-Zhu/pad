def solution():
    """There was only enough room for 21 people on a raft if no one wore life jackets. There were 7 fewer people who could fit on the raft if everyone wore life jackets. If 8 people on the raft needed life jackets, how many people could fit on the raft?"""
    raft_capacity_without_life_jackets = 21
    raft_capacity_with_life_jackets = raft_capacity_without_life_jackets - 7
    num_people_with_life_jackets = 8
    num_people_without_life_jackets = raft_capacity_without_life_jackets - num_people_with_life_jackets
    total_capacity = num_people_without_life_jackets + (num_people_with_life_jackets * 2)
    result = total_capacity
    return result

print(solution())