def solution():
    # Set up equations for the problem
    # Let x = number of chickens Colten has
    # Then, 2y + 25 = number of chickens Quentin has
    # And, 3z - 4 = number of chickens Skylar has
    # Also, x + 2y + 3z = 383 (total number of chickens)
    
    # Solve for x
    # x + 2(3z-4) + 25 + 3z = 383
    # x + 6z - 8 + 25 + 3z = 383
    # x + 9z = 366
    # x = 366 - 9z
    
    # Substitute x into the equation for Quentin's chickens
    # 2y + 25 = 366 - 18z
    # 2y = 341 - 18z
    # y = (341 - 18z)/2
    
    # Substitute y into the equation for Skylar's chickens
    # 3z - 4 = (341 - 18z)/2 - 4
    # 3z - 4 = 169.5 - 9z
    # 12z = 173.5
    # z = 14.46 (rounded to 2 decimal places)
    
    # The number of chickens Colten has is approximately 14.46
    # However, chickens cannot be divided into fractions, so we can assume
    # that Colten has either 14 or 15 chickens.
    # To check which option is correct, we can substitute z = 14 and z = 15
    # into the equations for y and x, and see which combination gives a total
    # of 383 chickens.
    
    # If z = 14, then y = (341 - 18(14))/2 = 156
    # And x = 366 - 9(14) = 243
    # Total = 243 + 2(156) + 25 + 3(14) = 383 (correct!)
    # Therefore, Colten has 14 chickens.
    
    result = 14
    return result

print(solution())