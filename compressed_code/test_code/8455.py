def solution():
    
    total_people = 2 + 10 + 7
    total_baskets = 15
    eggs_per_basket = 12
    total_eggs = total_baskets * eggs_per_basket
    eggs_per_person = total_eggs // total_people
    result = eggs_per_person
    return result

print(solution())