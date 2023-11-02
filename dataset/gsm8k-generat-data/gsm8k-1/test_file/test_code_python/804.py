def solution():
    """There are 10 quarts of tea left from the party. Four students each drank 1.5 quarts of tea and 16 students each drank 2 quarts of tea. How many gallons of tea were at the beginning of the party?"""
    remaining_quarts = 10
    num_four_students = 4
    num_sixteen_students = 16
    quarts_per_four = 1.5
    quarts_per_sixteen = 2
    total_quarts = remaining_quarts + num_four_students * quarts_per_four + num_sixteen_students * quarts_per_sixteen
    gallons = total_quarts / 4
    result = gallons
    return result

print(solution())