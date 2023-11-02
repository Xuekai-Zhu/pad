def solution():
    # Calculate the number of Oreos James has
    total_Oreos = 52
    jordan_Oreos = total_Oreos / 5  # since James has 7 more than 4 times the Oreos Jordan has, we can set up the equation J = 4J + 7 and solve for J
    james_Oreos = 4 * jordan_Oreos + 7
    result = james_Oreos
    return result

print(solution())