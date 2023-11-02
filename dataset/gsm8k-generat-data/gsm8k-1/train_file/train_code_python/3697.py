def solution():
    """Kenia has three times as many rats as Hunter and Elodie has together. If Elodie has 30 rats, 10 rats more than Hunter, calculate the total number of pets the three have together?"""
    elodie_rats = 30
    hunter_rats = elodie_rats - 10
    kenia_rats = hunter_rats * 3
    total_pets = elodie_rats + hunter_rats + kenia_rats
    result = total_pets
    return result

print(solution())