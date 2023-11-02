def solution():
    # Calculate the cost of the t-shirts
    tshirt_cost = 5 * 100
    # Calculate the total amount spent on pants and t-shirts
    total_amount = 1500 - tshirt_cost
    # Calculate the cost of each pair of pants
    pants_cost = total_amount / 4
    result = pants_cost
    return result

print(solution())