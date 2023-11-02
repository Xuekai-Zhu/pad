def solution():
    """Alex makes luxury dresses out of silk. Each dress needs 5 meters of silk and Alex has 600 meters of silk in storage. His friends also want to learn how to make these dresses so Alex gives all 5 of them 20 meters of silk each. He uses the rest to make dresses himself. How many dresses can Alex make?"""
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