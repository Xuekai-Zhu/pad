def solution():
    # Taylor has 4 pets
    taylor_pets = 4

    # First 3 friends have twice as many pets as Taylor
    friend_pets = taylor_pets * 2
    total_friend_pets = friend_pets * 3

    # Another 2 friends have 2 pets each
    total_other_friend_pets = 2 * 2

    # Total number of pets
    total_pets = taylor_pets + total_friend_pets + total_other_friend_pets
    result = total_pets
    return result

print(solution())