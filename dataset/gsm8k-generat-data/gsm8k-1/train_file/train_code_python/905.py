def solution():
    """The bus started its route. At its first stop, 7 people got on. At the second stop, 3 people got off, and 5 people got on. At the third stop, 2 people got off, and 4 people got on. How many passengers are now on the bus?"""
    passengers = 7
    passengers -= 3
    passengers += 5
    passengers -= 2
    passengers += 4
    result = passengers
    return result

print(solution())