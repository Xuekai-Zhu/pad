def solution():
    """There was only enough room for 21 people on a raft if no one wore life jackets. There were 7 fewer people who could fit on the raft if everyone wore life jackets. If 8 people on the raft needed life jackets, how many people could fit on the raft?"""
    # Define the initial capacity without life jackets
    capacity_without_life_jackets = 21

    # Define the number of people who need life jackets
    num_people_with_life_jackets = 8

    # Calculate the capacity with life jackets
    capacity_with_life_jackets = capacity_without_life_jackets - 7

    # Calculate the total capacity of the raft
    total_capacity = capacity_with_life_jackets + num_people_with_life_jackets

    # return the result
    result = total_capacity
    return result

print(solution())