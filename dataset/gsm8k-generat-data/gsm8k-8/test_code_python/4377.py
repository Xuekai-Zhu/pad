def solution():
    # Set up the equations using the given information
    # Let x be the number of pencils Candy has
    # Then, Caleb has 2x - 3 pencils
    # And, Calen has 2x + 2 pencils
    # We also know Calen lost 10 pencils and now has 10
    # Therefore, he originally had 20 pencils
    # We can use this to solve for x

    calen_original = 20
    calen_after_loss = 10
    caleb = 2 * x - 3
    calen = 2 * x + 2

    # Use the fact that Calen lost 10 pencils
    # to set up an equation and solve for x
    calen_original - 10 = calen_after_loss
    20 - 10 = 2*x + 2*x - 3 + 5
    10 = 4x - 1
    x = 11/4

    # Round x up to the nearest whole number
    # since we're dealing with pencils
    x = round(x)
    candy = x
    result = candy
    return result

print(solution())