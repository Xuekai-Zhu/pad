def solution():
    """At a spa, Iris spent $400 to do her hair, 1/4 as much to do a manicure, and 3/4 as much money as a manicure to do a pedicure. How much money did she spend at the spa?"""
    hair_cost = 400
    manicure_cost = hair_cost / 4
    pedicure_cost = manicure_cost * 3 / 4
    total_cost = hair_cost + manicure_cost + pedicure_cost
    result = total_cost
    return result

print(solution())