def solution():
    total_animals = 160
    frogs = 160
    dogs = total_animals - (frogs / 2)
    cats = dogs - (dogs * 0.2)
    result = frogs + dogs + cats
    
    return result

print(solution())