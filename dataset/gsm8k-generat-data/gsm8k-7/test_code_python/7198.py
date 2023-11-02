def solution():
    betty_marbles = 60
    stuart_percent = 0.4
    stuart_marbles = 80

    # Calculate the number of marbles Stuart got from Betty
    stuart_share = stuart_marbles - (1 + stuart_percent) * betty_marbles / stuart_percent

    # Calculate the number of marbles Stuart had initially
    stuart_initial = stuart_share / stuart_percent
    result = stuart_initial
    return result

print(solution())