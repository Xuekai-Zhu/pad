def solution():
    coin = True
    people = {
        "Angelica": True,
        "Tariq": True,
        "Ursula": False,
        "Nena": False
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