def solution():
    coin = True
    people = {
        "Myriam": False,
        "José": True,
        "Cecy": True,
        "Faisal": True
    }
    for person, flips in people.items():
        if flips:
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())