def solution():
    # Calculate the amount of food the dietitian ate
    ate = 3/4 * 40

    # Calculate the amount of food she did not eat
    not_ate = 40 - ate

    # Calculate the number of calories she exceeded the FDA recommendation by
    exceeded = ate - 25

    result = exceeded
    return result

print(solution())