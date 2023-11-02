def solution():
    
    starting_pets = 16
    lost_pets = 6
    remaining_pets = starting_pets - lost_pets
    percent_loss = 1/5
    pets_died = remaining_pets * percent_loss
    pets_left = remaining_pets - pets_died
    result = pets_left
    return result

print(solution())