def solution():
    coin = True
    people = {
        "Yessenia": False,
        "Geraldine": True,
        "Minerva": True,
        "Tanya": True
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