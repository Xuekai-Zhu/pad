def solution():
    cola = "Coca-Cola"
    alcohol = "rum"
    contains_caffeine = True
    promotes_insomnia = True
    if cola == "Coca-Cola" and alcohol == "rum" and contains_caffeine and not promotes_insomnia:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())