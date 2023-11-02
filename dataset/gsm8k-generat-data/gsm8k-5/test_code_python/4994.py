def solution():
    total_age = 132  # The combined age of Amy, Jeremy, and Chris is 132

    # Let's assume Jeremy's age is x
    # According to the problem, Amy's age is 1/3 of Jeremy's age, therefore Amy's age is x/3
    # Also, Chris's age is twice as old as Amy's age, therefore Chris's age is 2(x/3) = 2x/3

    # Add up the ages
    combined_age = x + x/3 + 2*x/3

    # Since the combined age is 132, we can solve for x
    x = total_age * 3 / 5

    # The age of Jeremy is x
    result = x
    return result

print(solution())