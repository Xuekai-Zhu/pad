def solution():
    elodie_rats = 30
    hunter_rats = elodie_rats - 10
    kenia_rats = 3 * (hunter_rats + elodie_rats)

    total_pets = elodie_rats + hunter_rats + kenia_rats
    result = total_pets
    return result

print(solution())