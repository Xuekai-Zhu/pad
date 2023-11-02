def solution():
    """Cleo and Ignacio placed 30 of their marbles in a jar on a Monday. They took 3/5 of the marbles from the jar the next day and divided them equally. On the third day, Cleo took 1/2 of the marbles remaining in the jars. How many marbles did Cleo have on the third day?"""
    total_marbles = 30
    marbles_taken = total_marbles * (3/5)
    marbles_left = total_marbles - marbles_taken
    marbles_divided = marbles_left / 2
    cleo_marbles = marbles_divided / 2
    result = cleo_marbles
    return result

print(solution())