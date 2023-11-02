def solution():
    num_adults = 2  # Mr. Smith and his wife
    num_seniors = 2  # Mr. Smith's parents
    num_children = 3
    adult_price = 30
    children_price = 15
    discount = 0.1

    # Calculate the total cost of the adult buffets
    adult_cost = num_adults * adult_price

    # Calculate the total cost of the senior citizen buffets
    senior_cost = num_seniors * adult_price * (1 - discount)

    # Calculate the total cost of the children's buffets
    children_cost = num_children * children_price

    # Calculate the total cost for the entire family
    total_cost = adult_cost + senior_cost + children_cost
    result = total_cost
    return result

print(solution())