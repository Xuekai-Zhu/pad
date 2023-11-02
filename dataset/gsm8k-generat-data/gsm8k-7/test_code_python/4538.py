def solution():
    num_dogs = 12
    paws_per_dog = 4

    # Calculate the number of dogs standing on their back legs
    num_back_legs_dogs = num_dogs / 2

    # Calculate the number of paws on the ground from dogs standing on their back legs
    back_legs_paws = num_back_legs_dogs * 2 # each dog has 2 back paws on the ground

    # Calculate the number of paws on the ground from dogs standing on all 4 legs
    all_legs_paws = (num_dogs - num_back_legs_dogs) * 4 # each dog has 4 paws on the ground

    # Calculate the total number of dog paws on the ground
    total_paws = back_legs_paws + all_legs_paws
    result = total_paws
    return result

print(solution())