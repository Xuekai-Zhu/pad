def solution():
    coin = True
    people = {
        "Neil": True,
        "Dani": False,
        "Eddie": True,
        "Marcelino": False
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