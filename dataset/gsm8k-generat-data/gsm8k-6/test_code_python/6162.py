def solution():
    # Let x be the cost of pencils 
    # Then the cost of 2 erasers is (1/2)x
    # The total cost of 20 pencils and 40 erasers is 80
    # We can write an equation: 20x + 40 * (1/2)x = 80
    # Simplifying it, we get: 30x = 80
    # Therefore, x = 8/3, which is the cost of one pencil
    # The cost of 2 erasers is (1/2)x = (1/2)*(8/3) = 4/3
    result = round(4/3, 2) # rounding to 2 decimal places
    return result

print(solution())