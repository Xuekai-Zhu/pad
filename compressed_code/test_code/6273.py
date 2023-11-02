def solution():
    
    silk_per_dress = 5
    total_silk = 600
    friends = 5
    silk_given_to_friends = 20
    silk_used_for_friends = friends * silk_given_to_friends
    silk_left = total_silk - silk_used_for_friends
    dresses = silk_left // silk_per_dress
    result = dresses
    return result

print(solution())