def solution():
    # Calculate the total cost of the dolls
    doll_cost = 4 * 15

    # Calculate the amount Tonya can spend on each sister
    total_spend = doll_cost * 2
    spend_per_sister = total_spend / 2

    # Calculate the number of lego sets she can buy
    lego_cost = 20
    num_legos = spend_per_sister // lego_cost
    result = num_legos
    return result

print(solution())