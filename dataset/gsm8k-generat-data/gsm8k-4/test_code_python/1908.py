def solution():
    """Taylor and his friends decide to bring their pets together for a walk. 3 of his friends come first, each having twice as many pets as Taylor has. Another two of his friends have 2 pets each. If Taylor has 4 pets, what's the total number of pets they have together?"""
    # Define the number of pets Taylor has
    taylor_pets = 4

    # Calculate the number of pets each of the first three friends has
    friend_pets = taylor_pets * 2
    total_friend_pets = friend_pets * 3

    # Calculate the number of pets the two other friends have
    other_friend_pets = 2 * 2

    # Calculate the total number of pets
    total_pets = taylor_pets + total_friend_pets + other_friend_pets

    # return the result
    result = total_pets
    return result

print(solution())