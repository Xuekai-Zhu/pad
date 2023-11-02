def solution():
    """There was only enough room for 21 people on a raft if no one wore life jackets. There were 7 fewer people who could fit on the raft if everyone wore life jackets. If 8 people on the raft needed life jackets, how many people could fit on the raft?"""
    # Define the number of people who can fit on the raft without life jackets
    max_capacity = 21

    # Define the number of people who can fit on the raft with life jackets
    capacity_with_jackets = max_capacity - 7

    # Calculate the number of people who can fit on the raft with life jackets and 8 people wearing jackets
    actual_capacity = capacity_with_jackets + 8

    # Display the actual capacity of the raft
    result = actual_capacity
    return result

print(solution())