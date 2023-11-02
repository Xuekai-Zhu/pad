def solution():
    """Jack is stranded on a desert island. He wants some salt to season his fish. He collects 2 liters of seawater in an old bucket. If the water is 20% salt, how many ml of salt will Jack get when all the water evaporates?"""
    seawater_volume = 2000  # ml
    salt_concentration = 0.2
    salt_volume = seawater_volume * salt_concentration
    result = salt_volume
    return result

print(solution())