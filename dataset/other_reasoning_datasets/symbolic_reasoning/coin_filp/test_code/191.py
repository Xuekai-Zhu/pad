def solution():
    coin = True
    people = {
        "Manuel": True,
        "Aurelio": False,
        "India": True,
        "Rosalba": True
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