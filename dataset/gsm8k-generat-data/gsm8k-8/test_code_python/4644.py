def solution():
    # Define the number of gallons that Roman used
    roman_gallons = x

    # Define the number of gallons that Remy used, in terms of x
    remy_gallons = 3*x + 1

    # Calculate the total gallons used
    total_gallons = roman_gallons + remy_gallons

    # Set up an equation to solve for x
    # roman_gallons + remy_gallons = total_gallons
    # x + 3*x + 1 = 33
    # 4*x + 1 = 33
    # 4*x = 32
    # x = 8

    # Calculate the number of gallons that Remy used
    remy_gallons = 3*8 + 1
    result = remy_gallons
    return result

print(solution())