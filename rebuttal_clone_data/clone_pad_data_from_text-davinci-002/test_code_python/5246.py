def solution():
    dogs = [1, 2, 3]
    time = [10, 7, 9]
    charge_per_dog = 20
    charge_per_minute = 1
    total_charge = 0
    for i in range(len(dogs)):
        dog_charge = dogs[i] * charge_per_dog
        time_charge = time[i] * charge_per_minute
        total_charge += dog_charge + time_charge
    result = total_charge
    return result

print(solution())