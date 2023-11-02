def solution():
    tree_cost = 90  # The tree costs $90 to plant
    lemons_per_year = 7  # Each year it will grow 7 lemons
    selling_price = 1.5  # The lemon tree sells for $1.5 each
    cost_per_year = 3  # It costs $3 a year to water and feed the tree

    # Calculate the total revenue from selling lemons
    revenue = lemons_per_year * selling_price

    # Calculate the number of years it will take to reach the tree cost
    years = revenue / cost_per_year
    result = years
    return result

print(solution())