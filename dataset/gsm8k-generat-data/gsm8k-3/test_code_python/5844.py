def solution():
    """There are 3 consecutive odd integers that have a sum of -147. What is the largest number?"""
    # Let x be the smallest of the three consecutive odd integers, then the other two can be represented as x+2 and x+4
    # The sum of the three integers is -147, so we can write an equation as x + (x+2) + (x+4) = -147
    # Simplifying the equation, we get 3x + 6 = -147
    # Solving for x, we get x = -51
    # Therefore, the three consecutive odd integers are -51, -49, and -47, and the largest number is -47
    
    largest_number = -47
    result = largest_number
    return result

print(solution())