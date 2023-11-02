def solution():
    total_dogs = 12  # There are 12 dogs on stage
    half_dogs = total_dogs / 2  # Half of the dogs are standing on their back legs
    paws_on_ground = half_dogs * 4 + half_dogs * 2 # Calculate the total number of dog paws on the ground

    result = paws_on_ground
    return result

print(solution())