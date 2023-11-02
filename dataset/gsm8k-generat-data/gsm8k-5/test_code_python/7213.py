def solution():
    taco_grande_price = 10  # The price of the Taco Grande Plate
    side_salad_price = 2  # The price of a side salad
    cheesy_fries_price = 4  # The price of a plate of cheesy fries
    diet_cola_price = 2  # The price of a diet cola

    # Calculate Mike's total bill
    mike_bill = taco_grande_price + side_salad_price + cheesy_fries_price + diet_cola_price

    # Calculate John's bill
    john_bill = taco_grande_price

    # Calculate the combined total cost of Mike and John's lunch
    total_cost = mike_bill + john_bill
    result = total_cost
    return result

print(solution())