def solution():
    """Taylor and his friends decide to bring their pets together for a walk. 3 of his friends come first, each having twice as many pets as Taylor has. Another two of his friends have 2 pets each. If Taylor has 4 pets, what's the total number of pets they have together?"""
    taylor_pets = 4
    friend1_pets = 2*taylor_pets
    friend2_pets = 2*taylor_pets
    friend3_pets = 2*taylor_pets
    friend4_pets = 2
    friend5_pets = 2
    total_pets = taylor_pets + friend1_pets + friend2_pets + friend3_pets + friend4_pets + friend5_pets
    result = total_pets
    return result

print(solution())