def solution():
    coin = True
    people = {
        "Diego": False,
        "Val": True,
        "Vincent": False,
        "Stacie": False
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