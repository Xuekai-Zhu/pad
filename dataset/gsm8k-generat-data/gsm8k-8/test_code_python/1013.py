def solution():
    # Define the cost and quantity of the long-sleeved jerseys
    long_sleeve_cost = 15
    long_sleeve_quantity = 4

    # Calculate the total cost of the long-sleeved jerseys
    long_sleeve_total_cost = long_sleeve_cost * long_sleeve_quantity

    # Define the cost of one striped jersey
    striped_cost = 10

    # Calculate the quantity of striped jerseys purchased
    striped_quantity = (80 - long_sleeve_total_cost) / striped_cost

    result = striped_quantity
    return result

print(solution())