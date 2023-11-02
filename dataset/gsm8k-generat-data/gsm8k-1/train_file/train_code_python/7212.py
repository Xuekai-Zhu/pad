def solution():
    """Mike and John dined at the Taco Palace restaurant. They each ordered the Taco Grande Plate as their main meal, but Mike also ordered a side salad for $2, a plate of cheesy fries for $4, and a diet cola for $2. As a result, Mike's lunch bill was twice as large as John's bill. What was the combined total cost, in dollars, of Mike and John's lunch?"""
    taco_grande_plate_cost = 10
    mike_side_salad_cost = 2
    mike_cheesy_fries_cost = 4
    mike_diet_cola_cost = 2
    mike_total_cost = taco_grande_plate_cost + mike_side_salad_cost + mike_cheesy_fries_cost + mike_diet_cola_cost
    john_total_cost = taco_grande_plate_cost
    combined_cost = mike_total_cost + john_total_cost
    result = combined_cost
    return result

print(solution())