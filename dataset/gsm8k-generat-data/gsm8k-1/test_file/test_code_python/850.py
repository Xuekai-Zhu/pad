def solution():
    """A local town is expanding and wants to build several new homes across the next three years. In the first year, they will build 12 homes. In the next year, they will build three times this many homes. In the third year, they will count how many homes they have built and double the amount. How many homes will the town have built over the next three years?"""
    year1_homes = 12
    year2_homes = 3 * year1_homes
    year3_homes = 2 * (year1_homes + year2_homes)
    total_homes = year1_homes + year2_homes + year3_homes
    result = total_homes
    return result

print(solution())