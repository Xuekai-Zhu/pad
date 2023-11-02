def solution():
    coin = True
    people = {
        "Denny": True,
        "Carlo": True,
        "Reinaldo": True,
        "Jessi": True
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