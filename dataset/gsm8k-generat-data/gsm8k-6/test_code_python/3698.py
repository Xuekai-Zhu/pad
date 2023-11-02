def solution():
    # Calculate Hunter's number of rats
    hunter_rats = 30 - 10 

    # Calculate the total number of rats that Hunter and Elodie have together
    hunter_and_elodie_rats = hunter_rats + 30 

    # Calculate Kenia's number of rats
    kenia_rats = 3 * hunter_and_elodie_rats 

    # Calculate the total number of pets the three have together
    total_pets = kenia_rats + hunter_and_elodie_rats + 30 
    result = total_pets
    return result

print(solution())