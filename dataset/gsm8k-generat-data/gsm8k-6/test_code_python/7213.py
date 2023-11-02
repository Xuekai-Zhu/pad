def solution():
    taco_grande_plate = 8  # cost of Taco Grande Plate
    john_bill = taco_grande_plate  # John only ordered the Taco Grande Plate
    mike_bill = 2 + 4 + 2 + taco_grande_plate  # Mike ordered Taco Grande Plate, side salad, cheesy fries, and diet cola
    total_bill = john_bill + mike_bill  # combined total cost of Mike and John's lunch
    # Find the value of Taco Grande Plate such that Mike's bill is twice John's bill
    value_of_taco_grande_plate = total_bill / 4
    result = total_bill
    return result

print(solution())