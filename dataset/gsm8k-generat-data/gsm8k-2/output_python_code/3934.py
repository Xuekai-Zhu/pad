def solution():
    """Karen works at an animal shelter with 30 dogs, 28 cats, and 20 lizards. Every month, 50% of the dogs are adopted, 25% of the cats are adopted, and 20% of lizards are adopted. If the shelter takes in 13 new pets a month, how many pets are there after one month?"""
    dog_count = 30
    cat_count = 28
    lizard_count = 20
    new_pets = 13
    
    # Calculate number of adoptions
    dogs_adopted = 0.5 * dog_count
    cats_adopted = 0.25 * cat_count
    lizards_adopted = 0.2 * lizard_count
    
    # Update animal counts after adoptions
    dog_count -= dogs_adopted
    cat_count -= cats_adopted
    lizard_count -= lizards_adopted
    
    # Add new pets to animal counts
    dog_count += new_pets // 2
    cat_count += new_pets // 4
    lizard_count += new_pets // 5
    
    # Calculate total animal count after one month
    total_count = dog_count + cat_count + lizard_count
    
    result = total_count
    return result

print(solution())