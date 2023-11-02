def solution():
    """ A box has 2 dozen water bottles and half a dozen more apple bottles than water bottles. How many bottles are in the box?"""
    water_bottles = 2*12
    apple_bottles = water_bottles + 0.5*12
    total_bottles = water_bottles + apple_bottles
    result = total_bottles
    return result

print(solution())