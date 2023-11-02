def solution():
    """Alex makes luxury dresses out of silk. Each dress needs 5 meters of silk and Alex has 600 meters of silk in storage. His friends also want to learn how to make these dresses so Alex gives all 5 of them 20 meters of silk each. He uses the rest to make dresses himself. How many dresses can Alex make?"""
    silk_per_dress = 5
    total_silk = 600
    silk_given_to_friends = 5 * 20
    silk_for_alex = total_silk - silk_given_to_friends
    dresses = silk_for_alex // silk_per_dress
    result = dresses
    return result

print(solution())