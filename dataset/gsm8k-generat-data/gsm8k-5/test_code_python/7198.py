def solution():
    bettys_marbles = 60 # Betty had 60 marbles
    stuart_marbles_after = 80 # Stuart had 80 marbles after receiving 40% of Betty's collection

    # Calculate how many marbles Stuart received
    stuart_received = stuart_marbles_after - 0.6 * bettys_marbles

    # Calculate how many marbles Stuart originally had
    stuart_marbles_initial = stuart_received / 0.4
    result = stuart_marbles_initial
    return result

print(solution())