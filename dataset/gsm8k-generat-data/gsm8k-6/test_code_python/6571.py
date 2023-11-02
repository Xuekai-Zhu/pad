def solution():
    # Set up the initial number of marbles for Sam and Steve
    steve_marbles = x
    sam_marbles = 2 * steve_marbles
    sally_marbles = sam_marbles - 5

    # Perform the marble exchange between Sam, Sally, and Steve
    sam_marbles -= 3 * 2
    sally_marbles += 3
    steve_marbles += 3

    # Check if Sam has 8 marbles left and solve for Steve's current number of marbles
    if sam_marbles == 8:
        steve_marbles = (8 + 3 * 2 - sally_marbles) / 2
        result = steve_marbles
    else:
        result = "Incorrect initial values or marble exchange"

    return result

print(solution())