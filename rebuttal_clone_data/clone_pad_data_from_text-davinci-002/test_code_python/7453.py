def solution():
    friends_of_james = 75
    friends_of_john = friends_of_james * 3
    shared_friends = 25
    total_friends = friends_of_james + friends_of_john - shared_friends
    result = total_friends
    return result

print(solution())