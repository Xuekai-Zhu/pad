def solution():
    num_pencils = 20
    pencil_cost = 4  # assuming each pencil costs $4

    # Calculate the total cost of all pencils
    total_pencil_cost = num_pencils * pencil_cost

    # Calculate the cost of one eraser
    eraser_cost = pencil_cost / 2

    # Calculate the total cost of all erasers
    num_erasers = num_pencils * 2
    total_eraser_cost = num_erasers * eraser_cost

    # Calculate the total revenue earned from selling pencils and erasers
    total_revenue = 80

    # Calculate the total cost of all products sold
    total_cost = total_pencil_cost + total_eraser_cost

    # Subtract the total cost from the total revenue to get the profit
    profit = total_revenue - total_cost

    # Solve for the cost of one eraser using the profit equation
    eraser_cost = (profit - num_pencils * pencil_cost) / (2 * num_pencils)
    result = eraser_cost
    return result

print(solution())