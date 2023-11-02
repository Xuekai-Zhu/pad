def solution():
    friends = 10
    friends_dropping_out = 4
    remaining_friends = friends - friends_dropping_out
    share_increase = 8
    total_cost = remaining_friends * share_increase
    result = total_cost
    return result

print(solution())