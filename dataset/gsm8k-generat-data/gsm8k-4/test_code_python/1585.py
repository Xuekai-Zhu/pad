def solution():
    """Olly wants to get shoes to protect his pets’ paws. He owns 3 dogs, 2 cats, and a ferret. How many shoes does he need?"""
    
    # Define the number of shoes needed per pet
    SHOES_PER_PET = 4
    
    # Calculate the total number of pets
    total_pets = 3 + 2 + 1
    
    # Calculate the total number of shoes needed
    total_shoes = total_pets * SHOES_PER_PET
    
    # Return the result
    result = total_shoes
    return result

print(solution())