def solution():
    # Calculate the cost per bagel when buying individually
    individual_cost = 2.25

    # Calculate the cost per bagel when buying a dozen
    dozen_cost = 24/12

    # Calculate the savings per bagel when buying a dozen
    savings = individual_cost - dozen_cost

    # Convert savings to cents
    savings_in_cents = savings * 100

    result = savings_in_cents
    return result

print(solution())