def solution():
    # Calculate the number of turtle statues on Grandma Molly's front lawn after 4 years
    year_1 = 4  # number of statues created in year 1
    year_2 = 4 * year_1  # number of statues on the lawn after year 2
    year_3 = year_2 + 12 - 3  # number of statues on the lawn after year 3, accounting for the 3 broken ones
    year_4 = year_3 + 2 * 3  # number of statues on the lawn after year 4, adding twice as many new statues as were broken in year 3
    total_statues = year_1 + year_2 + year_3 + year_4  # total number of statues over the 4 years
    result = total_statues
    return result

print(solution())