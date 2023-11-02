def solution():
    
    pizza_slices = 12
    slices_per_person = 4
    total_people = pizza_slices // slices_per_person
    result = total_people - 1
    return result

print(solution())