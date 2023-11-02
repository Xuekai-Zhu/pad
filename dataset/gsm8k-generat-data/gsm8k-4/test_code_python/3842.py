def solution():
    """Mark bought a shirt, pants, and shoes for $340. What is the price of the pants knowing that the price of a shirt is three-quarters of the price of the pants and that the price of a shoe is ten dollars more than the price of the pants?"""
    # Define the price of the shirt as a fraction of the price of the pants
    shirt_price = 3/4

    # Define the price of the shoes as a difference from the price of the pants
    shoe_price = 10

    # Define the total cost of the three items and the number of items
    total_cost = 340
    num_items = 3

    # Solve the system of equations to find the price of the pants
    a = np.array([[1, shirt_price, 1], [1, 1, shirt_price + shoe_price], [1, 0, 0]])
    b = np.array([total_cost, total_cost, 0])
    solution = np.linalg.solve(a, b)

    # Extract the price of the pants from the solution
    pants_price = solution[1]

    result = pants_price
    return result

print(solution())