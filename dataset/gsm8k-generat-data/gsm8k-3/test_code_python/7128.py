def solution():
    """Blake needs to prime and paint 5 rooms in his house.  Each room will require a gallon of primer and a gallon of paint.  Currently the primer is $30.00 a gallon and they are offering 20% off.  The paint costs $25.00 a gallon and is not on sale.  How much will he spend on paint and primer?"""
    # Define the cost of primer and paint
    PRIMER_COST = 30
    PAINT_COST = 25

    # Define the number of rooms to be painted
    rooms = 5

    # Calculate the total cost of primer
    primer_cost = PRIMER_COST * rooms * 0.8

    # Calculate the total cost of paint
    paint_cost = PAINT_COST * rooms

    # Calculate the total cost of both primer and paint
    total_cost = primer_cost + paint_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())