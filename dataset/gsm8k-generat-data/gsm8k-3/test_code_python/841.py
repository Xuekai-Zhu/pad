def solution():
    """Heloise has dogs and cats in the ratio of 10:17, with the total number of pets being 189. If she gives 10 dogs to her friend Janet, how many dogs does she remain with altogether?"""
    # Define the ratio of dogs to cats
    DOG_CAT_RATIO = 10 / 17

    # Calculate the total number of pets
    total_pets = 189

    # Calculate the number of dogs
    dogs = DOG_CAT_RATIO * total_pets

    # Calculate the number of cats
    cats = total_pets - dogs

    # Subtract 10 dogs given to Janet from the total number of dogs
    remaining_dogs = dogs - 10

    # Display the number of remaining dogs
    result = remaining_dogs
    return result

print(solution())