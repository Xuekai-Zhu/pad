def solution():
    coin = True
    people = {
        "Buddy": True,
        "Violet": False,
        "Johana": True,
        "Tina": False
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