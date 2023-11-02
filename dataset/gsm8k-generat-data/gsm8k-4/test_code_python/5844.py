def solution():
    """There are 3 consecutive odd integers that have a sum of -147. What is the largest number?"""
    # Let's assume the first odd integer to be x
    # Then the second and the third consecutive odd integers will be x+2 and x+4 respectively
    # Since the sum of these 3 integers is -147, we can write an equation as follows:
    # x + (x+2) + (x+4) = -147
    # Solving for x, we get:
    # 3x + 6 = -147
    # 3x = -153
    # x = -51
    # Therefore, the first odd integer is -51, and the largest integer is -47

    largest_number = -47
    result = largest_number
    return result

print(solution())