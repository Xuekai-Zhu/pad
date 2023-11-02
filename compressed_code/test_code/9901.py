def solution():
    
    initial_animals = 10
    mom_gift = 2
    total_animals = initial_animals + mom_gift
    dad_gift = total_animals * 3
    total_animals += dad_gift
    result = total_animals
    return result

print(solution())