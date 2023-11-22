def solution():
    
    # Define the prices of the items
    croissant_price = 3.00
    cinnamon_price = 2.50
    mini_quich_price = 4.00
    blueberry_price = 1.00

    # Calculate the total cost of the items
    total_cost = (5 * croissant_price) + (4 * cinnamon_price) + (3 * mini_quich_price) + (13 * blueberry_price)

    # Calculate the discount
    discount = total_cost * 0.10

    # Calculate the final bill
    final_bill = total_cost - discount

    # return the result
    result = final_bill
    return result

print(solution())