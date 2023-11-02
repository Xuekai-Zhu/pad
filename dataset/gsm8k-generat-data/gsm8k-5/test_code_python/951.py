def solution():
    # Michonne invites 6 friends from school and 12 friends from her neighborhood
    initial_friends = 6 + 12

    # Each friend can bring 2 more friends
    additional_friends = initial_friends * 2

    # Total number of people at the party
    total_people = initial_friends + additional_friends
    result = total_people
    return result

print(solution())