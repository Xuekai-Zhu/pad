def solution():
    total_friends = 100
    kept_friends = total_friends * (40 / 100)
    contacted_friends = kept_friends * (50 / 100)
    removed_friends = contacted_friends - kept_friends
    result = kept_friends - removed_friends
    return result

print(solution())