def solution():
    """Samantha, Aira, and Joe received 6 rubber bands each after they divided their bands equally.  If Samantha had 5 more bands than Aira and Aira had 1 fewer band than Joe, how many rubber bands did Aira have?"""
    # Define the number of rubber bands each person received
    total_bands = 6 * 3

    # Define the relationship between the number of bands each person received
    s = a + 5
    a = j - 1

    # Substitute the relationship between a and j into s = a + 5
    s = (j - 1) + 5

    # Simplify the equation
    s = j + 4

    # Substitute s into the equation for total bands
    total_bands = j + 4 + j - 1 + j

    # Simplify the equation
    total_bands = 3j + 3

    # Solve for j
    j = (total_bands - 3) / 3

    # Solve for a
    a = j - 1

    # Display the number of rubber bands Aira had
    result = a
    return result

print(solution())