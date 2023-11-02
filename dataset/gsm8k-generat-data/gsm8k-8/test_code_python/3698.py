def solution():
    # Calculate the number of rats Hunter has
    hunter_rats = 30 - 10
    # Calculate the total number of rats Kenia has
    kenia_rats = 3 * (hunter_rats + 30)
    # Calculate the total number of pets the three have together
    total_pets = hunter_rats + 30 + kenia_rats
    result = total_pets
    return result

print(solution())