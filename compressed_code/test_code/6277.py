def solution():
    
    num_floors = 12
    num_apartments_per_floor = [6 if i < num_floors/2 else 5 for i in range(num_floors)]
    max_residents_per_apartment = 4
    total_residents = sum(num_apartments_per_floor) * max_residents_per_apartment
    result = total_residents
    return result

print(solution())