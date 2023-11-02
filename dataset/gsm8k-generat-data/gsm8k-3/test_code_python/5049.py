def solution():
    """Armand is playing a guessing game with his dad where he has to guess a number his dad is thinking of. His dad tells him that the number, when multiplied by 3, is three less than twice 51. What is the number?"""
    # Define the equation given by Armand's dad
    equation = 3 * x == 2 * 51 - 3

    # Solve for x
    x = (2 * 51 - 3) / 3

    # Display the value of x
    result = x
    return result

print(solution())