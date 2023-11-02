def solution():
    bottles_per_year = 12  # Juanita goes through 1 bottle of sunscreen a month for 12 months
    regular_price = 30.00  # Each bottle of sunscreen costs $30.00

    # Calculate the total cost of the sunscreen at regular price
    total_regular_cost = bottles_per_year * regular_price

    discount_percent = 30  # The website offers a 30% discount on the entire purchase
    discount_decimal = discount_percent / 100  # Convert the discount percentage to a decimal

    # Calculate the total cost of the sunscreen after the discount
    total_discounted_cost = total_regular_cost * (1 - discount_decimal)

    result = total_discounted_cost
    return result

print(solution())