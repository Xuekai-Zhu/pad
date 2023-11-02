def solution():
    coin = True
    people = {
        "Ángel": True,
        "Carlton": False,
        "Sameer": False,
        "Martinez": True
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