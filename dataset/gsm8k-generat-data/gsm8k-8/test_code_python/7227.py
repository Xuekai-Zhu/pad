def solution():
    # Define the cost of a pencil and a pen
    pencil_cost = 1.60
    pen_cost = 2

    # Define how many pens Elizabeth wants to buy
    num_pens = 6

    # Calculate how much money Elizabeth will spend on pens
    pen_total_cost = num_pens * pen_cost

    # Calculate how much money Elizabeth has left for pencils
    remaining_money = 20 - pen_total_cost

    # Calculate how many pencils Elizabeth can buy with the remaining money
    num_pencils = remaining_money / pencil_cost
    result = num_pencils
    return result

print(solution())