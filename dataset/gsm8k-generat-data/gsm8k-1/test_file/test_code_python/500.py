def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    bobbie_last_name = len("GREY") + 2
    samantha_last_name = bobbie_last_name - 3
    result = samantha_last_name
    return result


def solution():
    """Suzie loves to chew fruit-flavored gum. She bought four packs of gum the last time she was at the store. She got two packs of her favorite flavor, strawberry. She paid $2 for a pack of grape gum that she also liked. She wanted to try something new, so she paid half as much for a small pack of green apple gum. If she paid $7 in all, how many dollars did each pack of strawberry gum cost?"""
    total_packs = 4
    packs_of_strawberry = 2
    cost_of_grape = 2
    cost_of_green_apple = cost_of_strawberry / 2
    total_cost = 7
    cost_of_strawberry = (total_cost - (packs_of_strawberry * cost_of_strawberry) - cost_of_grape - cost_of_green_apple) / packs_of_strawberry
    result = cost_of_strawberry
    return result

print(solution())