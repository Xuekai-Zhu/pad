def solution():
    easy_rider_producer = "Peter Fonda"
    brooke_shields_princeton_boyfriend = "Dean Cain"
    wanda_nevada_cast = ["Brooke Shields", "Peter Fonda"]
    if easy_rider_producer == wanda_nevada_cast[1] and brooke_shields_princeton_boyfriend == wanda_nevada_cast[0]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())