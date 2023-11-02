def solution():
    coin = True
    people = {
        "Allyson": True,
        "Mara": False,
        "Jo": True,
        "Toni": False
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