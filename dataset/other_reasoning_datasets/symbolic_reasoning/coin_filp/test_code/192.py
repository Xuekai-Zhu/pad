def solution():
    coin = True
    people = {
      "Garrett": False,
      "Eva": False,
      "Joaquin": True,
      "Monique": False
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