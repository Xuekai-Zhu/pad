def solution():
    scary_movie = True
    intended_to_make_laugh = True
    adrenaline_produced_by_fear = True
    if scary_movie and intended_to_make_laugh and not adrenaline_produced_by_fear:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())