def solution():
    ancient_polytheistic_religions = ["Greek", "Roman", "Egyptian"]
    flying_spaghetti_monster = "not ancient"
    if flying_spaghetti_monster not in ancient_polytheistic_religions:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())