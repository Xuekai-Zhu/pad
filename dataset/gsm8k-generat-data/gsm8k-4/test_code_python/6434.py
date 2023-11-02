def solution():
    """Clive is buying olives for dinner. He has $10 to spend and needs 80 olives. A jar of 20 olives costs $1.50. How much change will Clive have when he buys what he needs?"""
    # Define the cost and quantity of olives
    OLIVE_COST = 1.5
    OLIVES_PER_JAR = 20
    REQUIRED_OLIVES = 80

    # Define the budget
    budget = 10

    # Calculate the number of jars required
    jars = REQUIRED_OLIVES / OLIVES_PER_JAR

    # Calculate the total cost of the olives
    total_cost = jars * OLIVE_COST

    # Calculate the change that Clive will have
    change = budget - total_cost

    result = change
    return result

print(solution())