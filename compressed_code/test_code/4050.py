def solution():
    
    initial_stuffed_animals = 10
    mom_gift = 2
    total_stuffed_animals = initial_stuffed_animals + mom_gift
    dad_gift = 3 * total_stuffed_animals
    total_stuffed_animals += dad_gift
    result = total_stuffed_animals
    return result

print(solution())