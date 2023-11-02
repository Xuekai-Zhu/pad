def solution():
    num_kids = 2
    num_friends = 10
    num_adults = 7

    total_people = num_kids + num_friends + num_adults

    num_baskets = 15
    num_eggs_per_basket = 12

    total_eggs = num_baskets * num_eggs_per_basket

    eggs_per_person = total_eggs / total_people

    result = eggs_per_person
    return result

print(solution())