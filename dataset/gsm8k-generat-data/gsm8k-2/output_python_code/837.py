def solution():
    """A boat carrying 20 sheep, 10 cows and 14 dogs capsized. 3 of the sheep drowned. Twice as many cows drowned as did sheep. All of the dogs made it to shore. How many total animals made it to the shore?"""
    sheep = 20
    cows = 10
    dogs = 14

    # update counts after the accident
    sheep -= 3
    cows -= 2 * 3

    # calculate total animals on the boat before the accident
    total = sheep + cows + dogs

    result = total
    return result

print(solution())