def solution():
    """Heloise has dogs and cats in the ratio of 10:17, with the total number of pets being 189. If she gives 10 dogs to her friend Janet, how many dogs does she remain with altogether?"""
    total_pets = 189
    dog_to_cat_ratio = 10 / 17
    
    # Calculate number of dogs and cats based on ratio
    total_ratio_parts = 10 + 17
    total_dogs = (10 / total_ratio_parts) * total_pets
    
    # Subtract 10 dogs given away
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    
    return result

print(solution())