def solution():
    """On a construction site, the Laker cement factory provided 500 bags of cement sold to Mr. Zander at $10 per bag. Mr. Zander also received twenty lorries of construction sand, each carrying 10 tons of sand, sold at $40 per ton. How much money did Mr. Zander pay for these construction materials?"""
    # Define the cost of cement per bag and the cost of sand per ton
    CEMENT_PRICE = 10
    SAND_PRICE = 40

    # Define the quantity of cement and sand purchased
    cement_qty = 500
    sand_qty = 20 * 10

    # Calculate the total cost of cement and sand
    cement_cost = cement_qty * CEMENT_PRICE
    sand_cost = sand_qty * SAND_PRICE

    # Calculate the total cost of all construction materials
    total_cost = cement_cost + sand_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())