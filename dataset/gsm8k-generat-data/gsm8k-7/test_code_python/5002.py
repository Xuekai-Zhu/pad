def solution():
    total_oreos = 36
    james_oreos = 3 + 2 * jordan_oreos
    jordan_oreos = (total_oreos - james_oreos) / 3
    result = jordan_oreos
    return result

print(solution())