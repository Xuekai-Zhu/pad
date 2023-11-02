def solution():
    total_oreos = 52  # Total number of Oreos
    jordan_oreos = (total_oreos - 7) / 5  # Jordan has 7 less than 4 times James' Oreos
    james_oreos = (4 * jordan_oreos) + 7  # James has 7 more than 4 times the number of Oreos Jordan has
    result = james_oreos
    return result

print(solution())