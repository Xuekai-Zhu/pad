def solution():
    """John has to replace the ball bearings for machines he works with.  He has 10 machines and they take 30 ball bearings each.  It normally costs $1 per ball bearing but right now there is a sale where they are only $.75.  Also since he is buying in bulk he gets a further 20% discount.  How much money did he save by buying them all during the sale rather than 1 at a time?"""
    # Define the number of machines and ball bearings per machine
    num_machines = 10
    num_bearings = 30

    # Define the regular and sale prices of a ball bearing
    regular_price = 1.0
    sale_price = 0.75

    # Calculate the total regular and sale prices of all the ball bearings
    regular_total = num_machines * num_bearings * regular_price
    sale_total = num_machines * num_bearings * sale_price

    # Calculate the bulk discount
    discount = 0.2
    sale_total *= (1 - discount)

    # Calculate the amount saved by buying during the sale
    saved = regular_total - sale_total

    # return the result
    result = saved
    return result

print(solution())