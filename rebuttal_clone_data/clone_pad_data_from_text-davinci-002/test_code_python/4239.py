def solution():
    total_guests = 10
    nonmeat_eating_guest = 1
    nonbread_eating_guest = 1
    burgers_per_guest = 3
    buns_per_burger = 1
    total_buns_needed = (total_guests - nonmeat_eating_guest - nonbread_eating_guest) * burgers_per_guest * buns_per_burger
    buns_per_package = 8
    total_packages_needed = total_buns_needed / buns_per_package
    result = total_packages_needed
    return result

print(solution())