def solution():
    coin = True
    people = {
        "Kennedy": True,
        "Ginny": False,
        "Iliana": True,
        "Sky": False
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