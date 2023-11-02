def solution():
    # Calculate the number of chickens that died
    chickens_died = 0.4 * 400  

    # Calculate the number of new chickens Carla bought
    new_chickens = 10 * chickens_died

    # Calculate the total number of chickens now
    total_chickens = 400 - chickens_died + new_chickens
    result = total_chickens
    return result

print(solution())