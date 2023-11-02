def solution():
    # Calculate the total number of pets owned by Taylor's friends who came first
    first_friends_pets = 3 * 2 * 4  # each of the first 3 friends has twice as many pets as Taylor

    # Calculate the total number of pets owned by the other two friends
    other_friends_pets = 2 * 2  # the other two friends have 2 pets each

    # Calculate the total number of pets owned by everybody
    total_pets = first_friends_pets + other_friends_pets + 4  # Taylor has 4 pets

    result = total_pets
    return result

print(solution())