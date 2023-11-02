def solution():
    fred_initial = 212
    jane = 307
    charles = 156

    # Calculate the total number of sheets of paper Fred has after Jane gave him some
    fred_total = fred_initial + jane

    # Subtract the number of sheets of paper Fred gave to Charles
    fred_left = fred_total - charles
    result = fred_left
    return result

print(solution())