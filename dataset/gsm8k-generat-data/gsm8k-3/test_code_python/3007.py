def solution():
    """Emily went to the store and bought art supplies for $20 and 2 skirts that cost the same amount of money. She spent a total of $50. How much did Emily pay for each of the skirts?"""
    # Define the cost of the art supplies
    ART_SUPPLIES_COST = 20

    # Define the total cost of Emily's purchase
    total_cost = 50

    # Calculate the cost of the two skirts
    skirts_cost = total_cost - ART_SUPPLIES_COST

    # Calculate the cost of each skirt
    skirt_cost = skirts_cost / 2

    # Display the cost of each skirt
    result = skirt_cost
    return result

print(solution())