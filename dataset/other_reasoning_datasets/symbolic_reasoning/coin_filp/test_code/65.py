def solution():
    coin = True
    people = {
        "Faustino": True,
        "Lamar": True,
        "Fransisco": True,
        "Rina": True
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