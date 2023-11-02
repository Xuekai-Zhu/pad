def solution():
    
    silk_per_dress = 5
    total_silk = 600
    silk_given_to_friends = 5 * 20
    silk_for_alex = total_silk - silk_given_to_friends
    dresses = silk_for_alex // silk_per_dress
    result = dresses
    return result

print(solution())