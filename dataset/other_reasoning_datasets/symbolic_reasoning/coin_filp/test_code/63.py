def solution():
    coin = True
    people = {
        "Amparo": True,
        "Gianna": False,
        "Dion": True,
        "Tessa": True
    }
    for person, flips in people.items():
        if flips:
            # Flip the coin by reversing its current state
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())