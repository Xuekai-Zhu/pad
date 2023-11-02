def solution():
    coin = True
    people = {
        "Leigh": True,
        "Mindy": True,
        "Rocky": False,
        "Lex": True
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