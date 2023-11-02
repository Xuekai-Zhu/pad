def solution():
    """Kenia has three times as many rats as Hunter and Elodie has together. If Elodie has 30 rats, 10 rats more than Hunter, calculate the total number of pets the three have together?"""

    # Calculate the number of rats Hunter has
    hunter_rats = 30 - 10

    # Calculate the number of rats Elodie and Hunter have together
    elodie_hunter_rats = hunter_rats + 30

    # Calculate the number of rats Kenia has
    kenia_rats = elodie_hunter_rats * 3

    # Calculate the total number of pets the three have together
    total_pets = hunter_rats + 30 + kenia_rats

    result = total_pets
    return result

print(solution())