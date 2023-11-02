def solution():
    # Calculate the total number of bones taken by the dogs
    total_bones = 3 + 2 + (2*2) + 1 + (2*1) # dogs 1-5 took 3, 2, 4, 1, and 2 bones respectively
    
    # The total number of bones in the pile is the same as the total number taken by the dogs
    result = total_bones
    return result

print(solution())