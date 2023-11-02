def solution():
    """Cleo and Ignacio placed 30 of their marbles in a jar on a Monday. They took 3/5 of the marbles from the jar the next day and divided them equally. On the third day, Cleo took 1/2 of the marbles remaining in the jars. How many marbles did Cleo have on the third day?"""
    jar_size = 30
    taken_marbles = jar_size * (3/5)
    remaining_marbles = jar_size - taken_marbles
    cleo_marbles = remaining_marbles / 2
    remaining_marbles = remaining_marbles - cleo_marbles
    cleo_marbles += (remaining_marbles / 2)
    result = cleo_marbles
    return result

print(solution())