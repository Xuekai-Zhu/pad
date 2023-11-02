def solution():
    """A party of 4 order 3 dozen oysters on the half shell for $15.00 a dozen, 2 pounds of steamed shrimp for $14.00 a pound and 2 pounds of fried clams for $13.50 a pound.  If they split the bill equally, how much will they each owe?"""
    # Define the prices and quantities of each item
    oyster_price = 15
    oyster_quantity = 3 * 12
    shrimp_price = 14
    shrimp_weight = 2
    clams_price = 13.5
    clams_weight = 2

    # Calculate the total cost of each item
    oyster_cost = oyster_price * oyster_quantity
    shrimp_cost = shrimp_price * shrimp_weight
    clams_cost = clams_price * clams_weight

    # Calculate the total cost of the meal
    total_cost = oyster_cost + shrimp_cost + clams_cost

    # Divide the total cost by the number of people to get the cost per person
    cost_per_person = total_cost / 4

    result = cost_per_person
    return result

print(solution())