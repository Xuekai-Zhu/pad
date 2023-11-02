def solution():
    Monday = 5
    Tuesday = 7
    Wednesday = Monday * 2
    Thursday = (Monday + Tuesday + Wednesday) / 2
    Friday = Monday + Tuesday + Wednesday + Thursday
    result = Friday
    return result

print(solution())