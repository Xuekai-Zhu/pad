def solution():
    """Clive is buying olives for dinner. He has $10 to spend and needs 80 olives. A jar of 20 olives costs $1.50. How much change will Clive have when he buys what he needs?"""
    # Define the cost and number of olives per jar
    COST_PER_JAR = 1.5
    OLIVES_PER_JAR = 20

    # Define the total number of olives needed
    total_olives = 80

    # Calculate the total number of jars needed
    total_jars = total_olives // OLIVES_PER_JAR
    if total_olives % OLIVES_PER_JAR != 0:
        total_jars += 1

    # Calculate the total cost of the olives
    total_cost = total_jars * COST_PER_JAR

    # Calculate the change
    change = 10 - total_cost

    # Display the change
    result = change
    return result

print(solution())