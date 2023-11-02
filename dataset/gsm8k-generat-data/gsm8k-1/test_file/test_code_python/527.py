def solution():
    """48 people are riding a bus. On the first stop, 8 passengers get off, and 5 times as many people as the number who got off from the bus get into the bus. On the second stop 21, passengers get off and 3 times fewer passengers get on. How many passengers are riding the bus after the second stop?"""
    initial_passengers = 48
    first_stop_off = 8
    first_stop_on = 5 * first_stop_off
    first_stop_total = initial_passengers - first_stop_off + first_stop_on
    second_stop_off = 21
    second_stop_on = 3 * (first_stop_total - second_stop_off)
    final_passengers = first_stop_total - second_stop_off + second_stop_on
    result = final_passengers
    return result

print(solution())