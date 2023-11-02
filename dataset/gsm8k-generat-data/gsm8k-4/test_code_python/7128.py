def solution():
    """Blake needs to prime and paint 5 rooms in his house. Each room will require a gallon of primer and a gallon of paint. Currently the primer is $30.00 a gallon and they are offering 20% off. The paint costs $25.00 a gallon and is not on sale. How much will he spend on paint and primer?"""
    # Define the number of rooms and the required amount of primer and paint
    num_rooms = 5
    primer_per_room = 1
    paint_per_room = 1

    # Calculate the cost of primer per gallon after the discount
    primer_cost = 30
    primer_discount = 0.2
    primer_cost_after_discount = primer_cost - (primer_cost * primer_discount)

    # Calculate the total cost of primer
    total_primer_cost = num_rooms * primer_per_room * primer_cost_after_discount

    # Calculate the total cost of paint
    paint_cost = 25
    total_paint_cost = num_rooms * paint_per_room * paint_cost

    # Calculate the total cost of paint and primer
    total_cost = total_primer_cost + total_paint_cost

    result = total_cost
    return result

print(solution())