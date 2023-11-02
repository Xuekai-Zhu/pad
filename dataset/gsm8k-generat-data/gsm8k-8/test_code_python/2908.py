def solution():
    # Calculate the total amount of money earned from the bake sale
    total_earnings = 400

    # Calculate the cost of ingredients
    ingredient_cost = 100

    # Calculate the remaining total after ingredient cost is subtracted
    remaining_total = total_earnings - ingredient_cost

    # Calculate the amount donated to the homeless shelter (half of remaining total plus $10)
    shelter_donation = 0.5 * remaining_total + 10

    result = shelter_donation
    return result

print(solution())