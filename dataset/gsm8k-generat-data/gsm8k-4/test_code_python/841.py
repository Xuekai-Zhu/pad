def solution():
    """Heloise has dogs and cats in the ratio of 10:17, with the total number of pets being 189. If she gives 10 dogs to her friend Janet, how many dogs does she remain with altogether?"""
    # Define the ratio of dogs to cats
    dog_to_cat_ratio = 10 / 17

    # Define the total number of pets
    total_pets = 189

    # Calculate the number of dogs and cats
    total_dogs = total_pets / (1 + dog_to_cat_ratio)
    total_cats = total_pets - total_dogs

    # Subtract 10 dogs given to Janet from the total number of dogs
    remaining_dogs = total_dogs - 10

    # return the result
    result = remaining_dogs
    return result

print(solution())