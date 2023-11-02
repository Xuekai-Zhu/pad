def solution():
    # Define variables
    large_animal_wax = 4
    small_animal_wax = 2
    small_to_large_ratio = 3
    small_animal_wax_used = 12
    
    # Calculate the number of small animals and large animals
    small_animals = small_to_large_ratio * 1
    large_animals = 1
    
    # Calculate the total number of sticks of wax used
    total_wax_used = (large_animals * large_animal_wax) + (small_animals * small_animal_wax_used)
    
    result = total_wax_used
    return result

print(solution())