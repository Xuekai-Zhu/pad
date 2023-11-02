def solution():
    # Let's assign x to Leah's age
    # Then Rachel's age is x+4
    # The sum of their ages is 34
    # So, x + (x+4) = 34

    # Solving the equation for x, we get:
    x = (34-4)/2  # Leah's age is (total sum of ages - 4) divided by 2
    rachel_age = x+4

    result = rachel_age
    return result

print(solution())