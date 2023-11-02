def solution():
    """There were 50 people on the city bus. At the first stop, 15 people got off. At the next stop 8 people got off and 2 got on. At the third stop, 4 people got off and 3 people got on. How many people are on the bus after the third stop?"""
    initial_passengers = 50
    passengers_first_stop = initial_passengers - 15
    passengers_second_stop = passengers_first_stop - 8 + 2
    passengers_third_stop = passengers_second_stop - 4 + 3
    result = passengers_third_stop
    return result

print(solution())