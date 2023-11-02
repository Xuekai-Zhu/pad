def solution():
    # Define the cost of a pencil and a pen
    pencil_cost = 0.25
    pen_cost = 0.15

    # Calculate the number of pencils Bowen buys
    pencils_bought = 40 * (2/5 + 1)

    # Calculate the total cost of the pencils and pens bought
    total_cost = (pencil_cost * pencils_bought) + (pen_cost * 40)

    result = total_cost
    return result

print(solution())