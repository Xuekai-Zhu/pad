def solution():
    total_lollipops = 12  # Sarah bought 12 lollipops
    total_cost = 300  # Sarah paid 3 dollars for the lollipops (1 dollar = 100 cents)
    portion_shared = total_lollipops / 4  # Sarah offered to share 1/4 of the lollipops
    cost_shared = total_cost / 4  # The cost of the shared lollipops is 1/4 of the total cost
    julie_payment = cost_shared  # Julie insists on reimbursing Sarah for the cost of the lollipops shared
    result = int(julie_payment)  # Convert the payment to cents and return as integer
    return result

print(solution())