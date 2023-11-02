def solution():
    
    frog_count = 160
    dog_count = frog_count / 2
    cat_count = 0.8 * dog_count
    total_animals = frog_count + dog_count + cat_count
    result = total_animals
    return result

print(solution())