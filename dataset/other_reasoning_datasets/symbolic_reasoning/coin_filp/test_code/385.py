def solution():
    coin = True
    people = {
        "Jeremiah": True,
        "Kelley": False,
        "Josue": False,
        "Veronica": False
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