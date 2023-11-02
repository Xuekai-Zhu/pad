def solution():
    # Calculate the total charge without discount
    total_charge = 74 + (2*2) + 42  # price of shoes, 2 pairs of socks, and a bag
    # Calculate the amount exceeding $100
    excess_amount = max(total_charge - 100, 0)  # if the total charge is less than $100, excess_amount will be 0
    # Calculate the discount on excess amount
    discount = 0.1 * excess_amount
    # Calculate the final amount to be paid by Jaco
    final_amount = total_charge - discount
    result = final_amount
    return result

print(solution())