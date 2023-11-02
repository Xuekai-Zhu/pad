def solution():
    brother_picked_per_basket = 15
    brother_num_baskets = 3
    kimberly_picked = brother_picked_per_basket * brother_num_baskets * 8
    parents_picked = kimberly_picked - 93

    total_picked = kimberly_picked + brother_picked_per_basket * brother_num_baskets + parents_picked

    num_people = 4  # Kimberly, brother, and parents
    num_strawberries_per_person = total_picked / num_people
    result = num_strawberries_per_person
    return result

print(solution())