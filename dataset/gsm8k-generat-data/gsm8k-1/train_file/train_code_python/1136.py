def solution():
    """James has 7 more than 4 times the number of Oreos Jordan has. If there are 52 Oreos total, how many does James have?"""
    total_oreos = 52
    jordan_oreos = total_oreos/(4+1)
    james_oreos = 7 + 4*jordan_oreos
    result = james_oreos
    return result

print(solution())