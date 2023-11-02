def solution():
    # Calculate the cost of canvas
    canvas_cost = 3 * 20  # Canvas costs three times more than the brushes

    # Calculate the total cost of materials
    total_cost = 20 + canvas_cost + (8 * 5)  # Brushes, canvas, and 5 liters of paint

    # Calculate the profit from selling the painting
    profit = 200 - total_cost
    result = profit
    return result

print(solution())