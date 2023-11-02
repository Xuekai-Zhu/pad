def solution():
    """ Cleo and Ignacio placed 30 of their marbles in a jar on a Monday. They took 3/5 of the marbles from the jar the next day and divided them equally. On the third day, Cleo took 1/2 of the marbles remaining in the jars. How many marbles did Cleo have on the third day? """
    # Define the number of marbles in the jar on the first day
    marbles_start = 30

    # Calculate the number of marbles taken from the jar on the second day
    marbles_taken = marbles_start * (3/5)

    # Calculate the number of marbles each person gets on the second day
    marbles_per_person = marbles_taken / 2

    # Calculate the number of marbles remaining in the jar on the third day
    marbles_remaining = marbles_start - marbles_taken + marbles_per_person

    # Calculate the number of marbles Cleo has on the third day
    cleo_marbles = marbles_remaining / 2

    # Display the number of marbles Cleo has on the third day
    result = cleo_marbles
    return result

print(solution())