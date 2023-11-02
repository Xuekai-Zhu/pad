def solution():
    num_people = 12
    dinner_plate_price = 6.0
    bowl_price = 5.0
    salad_plate_price = 4.0

    # Calculate the total cost of dinner plates
    total_dinner_plate_cost = num_people * dinner_plate_price

    # Calculate the total cost of bowls
    total_bowl_cost = num_people * bowl_price

    # Calculate the total cost of all items
    total_cost = total_dinner_plate_cost + total_bowl_cost
    result = total_cost
    return result

print(solution())