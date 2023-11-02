def solution():
    # Determine how many notebooks Jack had initially
    jack_initial = 8 + 13

    # Calculate how many notebooks Jack has left after giving away 5 and then 6
    jack_left = jack_initial - 5 - 6

    result = jack_left
    return result

print(solution())