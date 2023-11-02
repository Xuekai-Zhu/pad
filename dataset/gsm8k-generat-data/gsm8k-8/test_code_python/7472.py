def solution():
    # Set up the equation with Anika's age (A) and Maddie's age (M)
    A = 30
    M = A * (3/4)

    # Calculate their ages in 15 years
    A_15yrs = A + 15
    M_15yrs = M + 15

    # Calculate their average age in 15 years
    avg_age_15yrs = (A_15yrs + M_15yrs) / 2
    result = avg_age_15yrs
    return result

print(solution())