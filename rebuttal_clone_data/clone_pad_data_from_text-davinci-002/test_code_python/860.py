def solution():
    earl = 90
    fred = 48
    greg = 36
    fred_to_earl = 28
    greg_to_fred = 32
    earl_to_greg = 40
    greg = greg + fred_to_earl - greg_to_fred
    earl = earl + greg_to_fred - earl_to_greg
    result = earl + greg
    return result

print(solution())