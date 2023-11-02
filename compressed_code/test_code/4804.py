def solution():
    
    total_friends = 100
    keep_friends_percentage = 0.4
    contacted_friends = total_friends - int(total_friends * keep_friends_percentage)
    responded_percentage = 0.5
    non_responded_friends = contacted_friends - int(contacted_friends * responded_percentage)
    friends_left = total_friends - non_responded_friends
    result = friends_left
    return result

print(solution())