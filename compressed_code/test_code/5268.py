def solution():
    
    tiger_enclosures = 4
    zebra_enclosures = tiger_enclosures * 2
    giraffe_enclosures = zebra_enclosures * 3
    total_tigers = tiger_enclosures * 4
    total_zebras = zebra_enclosures * 10
    total_giraffes = giraffe_enclosures * 2
    total_animals = total_tigers + total_zebras + total_giraffes
    result = total_animals
    return result

print(solution())