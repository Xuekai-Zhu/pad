def solution():
    
    mark_weight = 150
    susan_weight = mark_weight - 20
    bob_weight = susan_weight * 2
    total_weight = mark_weight + susan_weight + bob_weight
    num_friends = 3
    average_weight = total_weight / num_friends
    result = average_weight
    return result

print(solution())