def solution():
    jars = 4  # John has 4 jars of caterpillars
    caterpillars_per_jar = 10  # Each jar has 10 caterpillars
    total_caterpillars = jars * caterpillars_per_jar  # Calculate the total number of caterpillars

    # Calculate the number of caterpillars that become butterflies
    butterflies = (100 - 40) / 100 * total_caterpillars

    # Calculate the total revenue from selling butterflies
    revenue = butterflies * 3

    result = revenue
    return result

print(solution())