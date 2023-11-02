def solution():
    """Taylor and his friends decide to bring their pets together for a walk. 3 of his friends come first, each having twice as many pets as Taylor has. Another two of his friends have 2 pets each. If Taylor has 4 pets, what's the total number of pets they have together?"""
    # Define the number of pets Taylor has
    taylor_pets = 4

    # Calculate the number of pets each of the first 3 friends has
    friend_pets = taylor_pets * 2
    # Calculate the total number of pets owned by the first 3 friends
    friend_total_pets = friend_pets * 3

    # Calculate the total number of pets owned by the last 2 friends
    last_two_friends_pets = 2 * 2

    # Calculate the total number of pets owned by everyone together
    total_pets = taylor_pets + friend_total_pets + last_two_friends_pets

    # Display the total number of pets
    result = total_pets
    return result

print(solution())