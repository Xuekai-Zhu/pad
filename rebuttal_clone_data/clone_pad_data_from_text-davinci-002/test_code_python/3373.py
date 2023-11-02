def solution():
    kids = 2
    kids_friends = 10
    adults = 7
    total_people = kids + kids_friends + adults
    baskets = 15
    eggs_per_basket = 12
    total_eggs = baskets * eggs_per_basket
    eggs_per_person = total_eggs / total_people
    result = eggs_per_person
    return result

print(solution())