def solution():
    """A party of 4 order 3 dozen oysters on the half shell for $15.00 a dozen, 2 pounds of steamed shrimp for $14.00 a pound and 2 pounds of fried clams for $13.50 a pound.  If they split the bill equally, how much will they each owe?"""
    # Define the cost of each item
    OYSTERS_PRICE = 15
    SHRIMP_PRICE = 14
    CLAMS_PRICE = 13.5

    # Define the quantity of each item
    OYSTERS_QUANTITY = 3 * 12
    SHRIMP_QUANTITY = 2
    CLAMS_QUANTITY = 2

    # Calculate the total cost
    total_cost = (OYSTERS_PRICE * OYSTERS_QUANTITY) + (SHRIMP_PRICE * SHRIMP_QUANTITY) + (CLAMS_PRICE * CLAMS_QUANTITY)

    # Divide the total cost among the 4 people
    cost_per_person = total_cost / 4

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())