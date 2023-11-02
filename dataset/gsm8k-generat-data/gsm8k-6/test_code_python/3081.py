def solution():
    # Calculate the size of the pea patch
    pea_patch = 6 * 5  # one sixth of the pea patch is 5 square feet, so the size of the pea patch is 6 times that amount
    
    # Calculate the size of the radish patch, which is half the size of the pea patch
    radish_patch = pea_patch / 2
    
    result = radish_patch
    return result

print(solution())