def solution():
    lemons_per_tree = 60  # A normal lemon tree produces 60 lemons per year
    increased_production = 1.5  # Jim's trees produce 50% more lemons per year
    grove_size = 50 * 30  # Jim's grove has 50 rows and 30 trees per row
    total_years = 5  # Jim wants to know how many lemons he will produce in 5 years

    # Calculate the total number of lemons produced by one tree in a year with increased production
    lemons_per_tree = lemons_per_tree * increased_production

    # Calculate the total number of lemons produced by one tree in 5 years
    lemons_per_tree_5years = lemons_per_tree * total_years

    # Calculate the total number of lemons produced by all trees in 5 years
    total_lemons = grove_size * lemons_per_tree_5years

    result = total_lemons
    return result

print(solution())