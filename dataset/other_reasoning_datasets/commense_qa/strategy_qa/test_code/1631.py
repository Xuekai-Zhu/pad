def solution():
    spoken_in_southern_china = True
    has_no_relation_to_japanese = True
    if spoken_in_southern_china and not has_no_relation_to_japanese:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())