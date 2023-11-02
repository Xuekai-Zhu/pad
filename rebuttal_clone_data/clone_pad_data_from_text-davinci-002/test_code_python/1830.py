def solution():
    people = 15
    pounds_per_person = 2
    bags_of_ice = people * pounds_per_person
    packs_of_ice = bags_of_ice / 10
    price_per_pack = 3.00
    total_spent = packs_of_ice * price_per_pack
    result = total_spent
    return result

print(solution())