def solution():
    # Start with the current number of cats
    current_cats = 20
    
    # Calculate the number of dogs now (twice the number of cats)
    current_dogs = 2 * current_cats
    
    # Subtract the 20 new dogs to get the original number of dogs
    original_dogs = current_dogs - 20
    
    # The original number of dogs was half the original number of cats
    original_cats = original_dogs * 2
    
    result = original_cats
    return result

print(solution())