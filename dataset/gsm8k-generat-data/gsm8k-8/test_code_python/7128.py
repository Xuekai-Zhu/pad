def solution():
    # Calculate the cost of primer per gallon after discount
    primer_cost = 30 * 0.8

    # Calculate the total cost of primer for 5 rooms
    total_primer_cost = primer_cost * 5

    # Calculate the total cost of paint for 5 rooms
    total_paint_cost = 25 * 5

    # Calculate the total cost of paint and primer for 5 rooms
    total_cost = total_primer_cost + total_paint_cost

    result = total_cost
    return result

print(solution())