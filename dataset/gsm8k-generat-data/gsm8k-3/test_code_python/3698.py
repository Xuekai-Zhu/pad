def solution():
    """Kenia has three times as many rats as Hunter and Elodie has together. If Elodie has 30 rats, 10 rats more than Hunter, calculate the total number of pets the three have together?"""
    # Calculate the number of rats Hunter has
    hunter_rats = 30 - 10

    # Calculate the number of rats Elodie and Hunter have together
    elodie_hunter_rats = 30 + hunter_rats

    # Calculate the number of rats Kenia has
    kenia_rats = 3 * elodie_hunter_rats

    # Calculate the total number of pets the three have together
    total_pets = kenia_rats + elodie_hunter_rats + hunter_rats

    # Display the total number of pets
    result = total_pets
    return result

print(solution())