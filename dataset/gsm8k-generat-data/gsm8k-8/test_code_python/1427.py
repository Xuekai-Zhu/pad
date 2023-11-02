def solution():
    # Define the initial number of dogs
    total_dogs = 200

    # Add the 100 dogs that were moved to the rescue center
    total_dogs += 100

    # Give out 40 animals for adoption
    total_dogs -= 40

    # After a month, 60 more dogs were adopted
    total_dogs -= 60

    # Calculate the final total number of dogs in the rescue center
    result = total_dogs
    
    return result

print(solution())