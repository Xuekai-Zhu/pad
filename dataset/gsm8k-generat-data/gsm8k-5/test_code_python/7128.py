def solution():
    rooms = 5  # Blake needs to paint 5 rooms
    gallons_per_room = 2  # Each room requires a gallon of primer and a gallon of paint
    primer_price = 30  # The primer costs $30.00 a gallon
    primer_discount = 0.2  # The primer is on sale for 20% off
    paint_price = 25  # The paint costs $25.00 a gallon

    # Calculate the total cost of primer
    primer_cost = primer_price * gallons_per_room * rooms
    primer_cost -= primer_cost * primer_discount  # Apply the discount

    # Calculate the total cost of paint
    paint_cost = paint_price * gallons_per_room * rooms

    # Calculate the total cost of paint and primer
    total_cost = primer_cost + paint_cost
    result = total_cost
    return result

print(solution())