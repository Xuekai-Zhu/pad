def solution():
    coin = True
    people = {
        "Jeannie": False,
        "Kenneth": False,
        "Porfirio": False,
        "Ezequiel": True
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