def solution():
    num_rooms = 5
    primer_price = 30.0
    primer_discount = 0.2  # 20% discount
    paint_price = 25.0

    # Calculate the total number of gallons of primer needed
    total_primer = num_rooms

    # Calculate the total cost of primer (with discount)
    total_primer_cost = total_primer * primer_price * (1 - primer_discount)

    # Calculate the total number of gallons of paint needed
    total_paint = num_rooms

    # Calculate the total cost of paint
    total_paint_cost = total_paint * paint_price

    # Calculate the total cost of both paint and primer
    total_cost = total_primer_cost + total_paint_cost
    result = total_cost
    return result

print(solution())