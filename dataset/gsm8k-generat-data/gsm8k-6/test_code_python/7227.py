def solution():
    # Calculate the total cost of the 6 pens
    pen_cost = 2 * 6  

    # Calculate the remaining amount of money after buying the pens
    remaining_money = 20 - pen_cost  

    # Calculate the number of pencils Elizabeth can buy
    num_pencils = remaining_money // 1.6  # using integer division to get the whole number of pencils
    result = num_pencils
    return result

print(solution())