def solution():
    # Set up the equations with variables
    a = j/3  # Amy is 1/3 the age of Jeremy
    c = 2*a  # Chris is twice as old as Amy
    age_sum = a + j + c  # the sum of their ages is 132

    # Solve for Jeremy's age
    j = (132 - c) / (1 + 1/3 + 2)
    result = j
    return result

print(solution())