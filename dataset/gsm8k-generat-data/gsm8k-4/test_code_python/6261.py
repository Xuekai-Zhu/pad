def solution():
    """At the same store, Peter bought 2 pairs of pants and 5 shirts for $62 total, and Jessica bought 2 shirts for $20 total. Each pair of pants cost the same price, and each shirt cost the same price. How much does 1 pair of pants cost?"""
    # Define the number of pants and shirts bought by Peter
    peter_pants = 2
    peter_shirts = 5

    # Define the number of shirts bought by Jessica
    jessica_shirts = 2

    # Define the total cost of Peter's purchase and the cost per shirt
    peter_total = 62
    shirt_cost = (peter_total - (peter_pants * x)) / peter_shirts

    # Define the total cost of Jessica's purchase and the cost per shirt
    jessica_total = 20
    jessica_shirt_cost = jessica_total / jessica_shirts

    # Calculate the cost per pair of pants
    pant_cost = (peter_total - (peter_shirts * shirt_cost)) / peter_pants

    # Return the cost per pair of pants
    result = pant_cost
    return result

print(solution())