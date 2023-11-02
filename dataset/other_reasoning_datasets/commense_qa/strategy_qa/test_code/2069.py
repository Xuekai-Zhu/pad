def solution():
    bob_marley_children = 9
    kublai_khan_children = 23
    bob_marley_children_singers = True
    kublai_khan_children_warlords = True
    if bob_marley_children_singers and not kublai_khan_children_warlords:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())