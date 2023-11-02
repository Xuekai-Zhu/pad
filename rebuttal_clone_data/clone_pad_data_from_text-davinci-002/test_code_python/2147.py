def solution():
    newborn_elephants = 10
    baby_hippos = newborn_elephants - 10
    total_hippos = baby_hippos / (5/7)
    total_animals = newborn_elephants + baby_hippos + total_hippos
    result = total_animals
    return result

print(solution())