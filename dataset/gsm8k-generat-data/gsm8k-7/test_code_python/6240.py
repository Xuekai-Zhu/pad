def solution():
    sum_of_ages = 36

    # Let's assume that Jerome's age is x
    # Then, Nina's age is (1/2)x, and Leonard's age is (1/2)x - 4
    # We can write an equation for the sum of their ages and solve for Leonard's age

    x = (sum_of_ages - 8) / 1.5  # Solving for x
    leonard_age = (1/2)*x - 4
    result = leonard_age
    return result

print(solution())