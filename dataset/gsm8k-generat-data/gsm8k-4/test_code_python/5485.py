def solution():
    """On a construction site, the Laker cement factory provided 500 bags of cement sold to Mr. Zander at $10 per bag. Mr. Zander also received twenty lorries of construction sand, each carrying 10 tons of sand, sold at $40 per ton. How much money did Mr. Zander pay for these construction materials?"""
    # Define the price and quantity of cement
    cement_price = 10
    cement_quantity = 500

    # Define the price and quantity of sand
    sand_price = 40
    sand_quantity = 20 * 10

    # Calculate the total cost of cement
    cement_cost = cement_price * cement_quantity

    # Calculate the total cost of sand
    sand_cost = sand_price * sand_quantity

    # Calculate the total cost of all construction materials
    total_cost = cement_cost + sand_cost
    
    # return the result
    return total_cost

print(solution())