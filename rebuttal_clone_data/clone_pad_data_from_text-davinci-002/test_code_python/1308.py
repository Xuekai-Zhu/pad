def solution():
    Monday = 0.5
    Tuesday = 4
    Wednesday = 0.25
    Thursday = Monday + Tuesday + Wednesday / 2
    Friday = 52 - Monday - Tuesday - Wednesday - Thursday
    result = Friday
    return result

print(solution())