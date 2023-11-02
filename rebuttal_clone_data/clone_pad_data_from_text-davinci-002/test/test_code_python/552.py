def solution():
    friends_from_school = 6
    friends_from_neighborhood = 12
    total_friends = friends_from_school + friends_from_neighborhood
    friends_bringing_friends = total_friends * 2
    total_attendees = total_friends + friends_bringing_friends
    result = total_attendees
    return result

print(solution())