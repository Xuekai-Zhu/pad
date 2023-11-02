def solution():
    """Taylor and his friends decide to bring their pets together for a walk. 3 of his friends come first, each having twice as many pets as Taylor has. Another two of his friends have 2 pets each. If Taylor has 4 pets, what's the total number of pets they have together?"""
    taylor_pets = 4
    friend_pets_1 = taylor_pets * 2 * 3
    friend_pets_2 = 2
    total_pets = taylor_pets + friend_pets_1 + friend_pets_2
    result = total_pets
    return result

print(solution())