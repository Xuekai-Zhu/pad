def solution():
    total_money = 20
    pen_cost = 2
    num_pens = 6
    pencil_cost = 1.6

    # Calculate the total cost of pens
    pen_total_cost = pen_cost * num_pens

    # Calculate the remaining money after buying pens
    money_left = total_money - pen_total_cost

    # Calculate the maximum number of pencils Elizabeth can buy with the remaining money
    num_pencils = money_left // pencil_cost
    result = num_pencils
    return result

print(solution())