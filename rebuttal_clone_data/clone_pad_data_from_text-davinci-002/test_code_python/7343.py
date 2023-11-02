def solution():
    total_revenue = 32
    number_of_pan = 2
    brownie_per_pan = 8
    total_brownie_sold = number_of_pan * brownie_per_pan
    cost_per_brownie = total_revenue / total_brownie_sold
    result = cost_per_brownie
    return result

print(solution())