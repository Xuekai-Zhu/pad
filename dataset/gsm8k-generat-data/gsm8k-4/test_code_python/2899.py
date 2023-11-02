def solution():
    """Mark went to a store where he spent one-half of his money, and then spent $14 more. He then went to another store where he spent one-third of his starting money, and then spent $16 more. If he then had no money left, how much did he have when he entered the first store?"""
    # Define the variables
    m = None  # starting money
    m1 = None  # money left after first store
    m2 = None  # money left after second store

    # Set up the system of equations
    # m/2 - 14 = m1
    # (2/3)*(m1 + 14) - 16 = m2
    # m2 = 0

    # Solve for m
    m = round((58/3), 2)

    result = m
    return result

print(solution())