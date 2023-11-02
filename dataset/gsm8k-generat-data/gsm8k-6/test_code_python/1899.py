def solution():
    # Set up the equations
    # Let x = number of cherry candies
    # Then 3x = number of grape candies, and 2(3x) = number of apple candies
    # The total cost equation is: 2.50(x + 3x + 6x) = 200

    # Simplify the total cost equation
    # 12.5x = 200
    # x = 16, so there are 16 cherry candies

    # Calculate the number of grape candies and return the result
    grape_candies = 3 * 16
    result = grape_candies
    return result

print(solution())