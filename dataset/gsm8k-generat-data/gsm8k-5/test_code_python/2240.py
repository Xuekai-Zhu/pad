def solution():
    # Let's call the price of one pint of frozen yogurt "x"
    # Then we know that 5 pints of frozen yogurt cost 5*x = 5x dollars
    # We also know that 2 packs of gum cost half as much as 1 pint of frozen yogurt, so 2*(0.5*x) = x dollars
    # And we know that 5 trays of jumbo shrimp cost 5*5 = 25 dollars
    # So we can write the equation: 5x + x + 25 = 55
    # Simplifying the equation, we get: 6x + 25 = 55
    # Subtracting 25 from both sides: 6x = 30
    # Dividing by 6: x = 5

    # Therefore, the price of one pint of frozen yogurt is $5
    result = 5
    return result

print(solution())