def solution():
    total_pets = 189  # Total number of pets
    ratio_dogs = 10  # Ratio of dogs to cats is 10:17
    ratio_cats = 17
    total_ratio = ratio_dogs + ratio_cats

    # Calculate the number of dogs Heloise has
    num_dogs = (ratio_dogs / total_ratio) * total_pets

    # After giving 10 dogs to Janet, Heloise remains with:
    remaining_dogs = num_dogs - 10
    result = remaining_dogs
    return result

print(solution())