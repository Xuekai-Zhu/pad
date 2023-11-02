def solution():
    # Calculate the amount of money John got from selling the PlayStation
    ps_value = 400
    ps_sold_for = 0.8 * ps_value  # John sold it for 20% less than its value

    # Calculate the total cost of the computer and accessories
    computer_cost = 700
    accessories_cost = 200
    total_cost = computer_cost + accessories_cost

    # Calculate the amount of money John had to pay out of his pocket
    money_out_of_pocket = total_cost - ps_sold_for
    result = money_out_of_pocket
    return result

print(solution())