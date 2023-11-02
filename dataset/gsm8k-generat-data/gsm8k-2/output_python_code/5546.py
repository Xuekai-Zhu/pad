def solution():
    """Frank has an apple tree in his backyard. 5 apples are hanging on the tree and 8 have fallen to the ground. If Frank's dog eats 3 of the apples off of the ground, how many apples are left?"""
    hanging_apples = 5
    fallen_apples = 8
    eaten_apples = 3
    remaining_apples = hanging_apples + fallen_apples - eaten_apples
    result = remaining_apples
    return result

print(solution())