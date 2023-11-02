def solution():
    santa_gives_presents_to_good_children = True
    joffrey_is_not_a_good_child = False
    if santa_gives_presents_to_good_children and not joffrey_is_not_a_good_child:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())