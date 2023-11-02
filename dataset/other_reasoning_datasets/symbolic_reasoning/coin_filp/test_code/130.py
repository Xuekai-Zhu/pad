def solution():
    coin = True
    people = {
        "Memo": True,
        "Joey": False,
        "Phil": True,
        "Samuel": True
    }
    for person, flips in people.items():
        if flips:
            coin = not coin  # flip the coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())