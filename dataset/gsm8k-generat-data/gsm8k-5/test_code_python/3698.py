def solution():
    # Calculate Hunter's number of rats
    hunter_rats = 30 - 10  # Elodie has 10 more rats than Hunter
    # Calculate Elodie's number of rats
    elodie_rats = 30
    # Calculate Kenia's number of rats
    kenia_rats = 3 * (hunter_rats + elodie_rats)
    # Calculate the total number of pets the three have together
    total_pets = hunter_rats + elodie_rats + kenia_rats
    result = total_pets
    return result

print(solution())