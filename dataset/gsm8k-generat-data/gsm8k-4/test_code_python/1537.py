def solution():
    """Antoinette weighs 7 less kilograms than twice Rupert's weight. Together they weigh 98 kilograms. How many kilograms does Antoinette weigh?"""
    # Define Antoinette's weight as a variable
    antoinette_weight = None

    # Define Rupert's weight as a variable
    rupert_weight = None

    # Define the sum of their weights
    total_weight = 98

    # Use algebra to solve for Antoinette's weight
    # A = 2R - 7
    # A + R = 98
    # Substituting the first equation into the second equation:
    # (2R - 7) + R = 98
    # 3R - 7 = 98
    # 3R = 105
    # R = 35
    # Substituting R into the first equation to solve for A:
    # A = 2(35) - 7
    # A = 63

    antoinette_weight = 63

    # Return the result
    result = antoinette_weight
    return result

print(solution())