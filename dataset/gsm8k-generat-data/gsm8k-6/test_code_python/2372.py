def solution():
    # Calculate the total cost for the adult buffet and children's buffet
    adult_cost = 30 * 2  # Mr. Smith and his wife
    children_cost = 15 * 3  # Mr. Smith's 3 children
    senior_discount = 0.1  # 10% discount for Mr. Smith's parents
    senior_cost = (30 * 2) * (1 - senior_discount)  # Mr. Smith's parents with discount
    total_cost = adult_cost + children_cost + senior_cost

    result = total_cost
    return result

print(solution())