def solution():
    num_adults = 2  # Mr. Smith and his wife are adults
    num_seniors = 2  # Mr. Smith's parents are senior citizens
    num_children = 3  # Mr. Smith has 3 children
    adult_price = 30  # Price of an adult buffet
    child_price = 15  # Price of a children's buffet
    senior_discount = 0.1  # 10% discount for seniors

    # Calculate the total cost for each type of guest
    total_adult_cost = num_adults * adult_price
    total_senior_cost = (1 - senior_discount) * num_seniors * adult_price
    total_child_cost = num_children * child_price

    # Calculate the total cost for Mr. Smith's family
    total_cost = total_adult_cost + total_senior_cost + total_child_cost
    result = total_cost
    return result

print(solution())