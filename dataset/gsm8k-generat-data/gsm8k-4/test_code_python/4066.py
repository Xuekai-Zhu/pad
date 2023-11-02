def solution():
    """Cleo and Ignacio placed 30 of their marbles in a jar on a Monday. They took 3/5 of the marbles from the jar the next day and divided them equally. On the third day, Cleo took 1/2 of the marbles remaining in the jars. How many marbles did Cleo have on the third day?"""
    # Define the initial number of marbles in the jar
    initial_marbles = 30

    # Calculate the number of marbles taken out on the second day
    taken_out = initial_marbles * (3/5)

    # Calculate the number of marbles remaining after being divided equally
    remaining = (initial_marbles - taken_out) / 2

    # Calculate the number of marbles Cleo took on the third day
    cleo_took = remaining / 2

    # Calculate the total number of marbles Cleo had on the third day
    total_marbles = remaining - cleo_took

    # Return the result
    result = total_marbles
    return result

print(solution())