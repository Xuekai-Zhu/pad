def solution():
    """James has 3 more than 2 times the number of Oreos Jordan has. If there are 36 Oreos total, how many does Jordan have?"""
    total_oreos = 36
    james_oreos = 2 * jordan_oreos + 3
    jordan_oreos = (total_oreos - 3) / 2
    result = jordan_oreos
    return result

print(solution())