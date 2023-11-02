def solution():
    roman_gallons = x  # Let's represent the number of gallons Roman used for his shower as x
    remy_gallons = 3*x + 1  # Remy used 1 more gallon than 3 times the number of gallons Roman used

    # Calculate the total number of gallons used by both boys
    total_gallons = roman_gallons + remy_gallons

    # Use the fact that the total gallons used was 33 to solve for x and then find remy_gallons
    x = (33 - 1) / 4  # Solving for x using the fact that remy_gallons = 3x + 1 and total_gallons = 33
    remy_gallons = 3*x + 1

    result = remy_gallons
    return result

print(solution())