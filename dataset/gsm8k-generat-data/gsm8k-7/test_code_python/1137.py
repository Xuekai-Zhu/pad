def solution():
    total_oreos = 52

    # Calculate the number of Oreos Jordan has
    jordan_oreos = total_oreos / 5  # 1/5th of the total amount of Oreos

    # Calculate the number of Oreos James has
    james_oreos = 4 * jordan_oreos + 7

    result = james_oreos
    return result

print(solution())