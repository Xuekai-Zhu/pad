def solution():
    good_king_wenceslas = True
    jolly_old_st_nicholas = True
    named_after_saints = False
    if good_king_wenceslas and jolly_old_st_nicholas:
        named_after_saints = True
    if named_after_saints:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())