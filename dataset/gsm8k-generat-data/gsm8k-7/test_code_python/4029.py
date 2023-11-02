def solution():
    pop_price = 1.5
    pop_cost = 0.9
    pencil_price = 1.8
    num_pencils = 100

    # Calculate the total cost of all pencils
    total_pencil_cost = num_pencils * pencil_price

    # Calculate the amount of money from each pop that goes toward buying pencils
    pencil_portion = pop_price - pop_cost

    # Calculate the number of pops needed to cover the cost of pencils
    num_pops = total_pencil_cost / pencil_portion
    result = num_pops
    return result

print(solution())