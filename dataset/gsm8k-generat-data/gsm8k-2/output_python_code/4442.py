def solution():
    """The carousel at the fair has 3 blue horses, three times that many purple horses, twice as many green horses as purple horses, and 1/6th as many gold horses as green horses. How many horses are there total?"""
    blue_horses = 3
    purple_horses = 3 * blue_horses
    green_horses = 2 * purple_horses
    gold_horses = green_horses / 6

    total_horses = blue_horses + purple_horses + green_horses + gold_horses
    result = total_horses
    return result

print(solution())