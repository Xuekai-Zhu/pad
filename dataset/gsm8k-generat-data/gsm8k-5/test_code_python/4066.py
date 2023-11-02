def solution():
    # Initially, there are 30 marbles in the jar
    marbles_in_jar = 30

    # On the second day, 3/5 of the marbles are taken out and divided equally
    marbles_taken_out = int(3/5 * marbles_in_jar)
    marbles_each = int(marbles_taken_out / 2)

    # Cleo takes 1/2 of the marbles remaining on the third day
    remaining_marbles = marbles_in_jar - marbles_taken_out + marbles_each
    cleo_marbles = int(remaining_marbles / 2)

    result = cleo_marbles
    return result

print(solution())