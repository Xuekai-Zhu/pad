def solution():
    """John raises butterflies.  He has 4 jars of 10 caterpillars each.  40% of them fail to become butterflies, but the rest become caterpillars.    He sells the butterflies for $3 each.  How much money does he make?"""
    # Define the number of jars and caterpillars per jar
    JARS = 4
    CATERPILLARS_PER_JAR = 10

    # Calculate the total number of caterpillars
    total_caterpillars = JARS * CATERPILLARS_PER_JAR

    # Calculate the number of caterpillars that fail to become butterflies
    failed_caterpillars = total_caterpillars * 0.4

    # Calculate the number of caterpillars that become butterflies
    butterflies = total_caterpillars - failed_caterpillars

    # Calculate the total revenue from selling the butterflies
    revenue = butterflies * 3

    # Display the revenue
    result = revenue
    return result

print(solution())