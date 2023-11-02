def solution():
    # Calculate the total fuel used between Nov 1, 2005 and Jan 1, 2006
    fuel_used_1 = 3000 - 180

    # Calculate the total fuel used between Jan 1, 2006 and May 1, 2006
    fuel_used_2 = 3000 - 1238

    # Calculate the total fuel used between Nov 1, 2005 and May 1, 2006
    total_fuel_used = fuel_used_1 + fuel_used_2

    result = total_fuel_used
    return result

print(solution())