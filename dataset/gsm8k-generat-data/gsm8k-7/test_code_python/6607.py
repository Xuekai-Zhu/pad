def solution():
    total_nails = 164
    nails_per_dog = 4
    
    # Calculate the total number of dogs if all of them had four legs
    total_dogs = total_nails / nails_per_dog
    
    # Deduct the number of dogs with three legs
    three_legged_dogs = 3
    four_legged_dogs = total_dogs - three_legged_dogs
    
    result = four_legged_dogs
    return result

print(solution())