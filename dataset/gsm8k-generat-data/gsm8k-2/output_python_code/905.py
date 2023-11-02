def solution():
    """The bus started its route. At its first stop, 7 people got on. At the second stop, 3 people got off, and 5 people got on. At the third stop, 2 people got off, and 4 people got on. How many passengers are now on the bus?"""
    initial_passengers = 0
    first_stop = 7
    second_stop = -3 + 5
    third_stop = -2 + 4
    total_passengers = initial_passengers + first_stop + second_stop + third_stop
    result = total_passengers
    return result

print(solution())