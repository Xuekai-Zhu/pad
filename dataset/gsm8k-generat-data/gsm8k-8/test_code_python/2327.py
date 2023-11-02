def solution():
    # Calculate the cost of training
    training_cost = 12 * 250

    # Calculate the total cost of adoption, training, and certification
    total_cost = 150 + training_cost + 3000*(1-0.9)

    # Calculate the out-of-pocket cost
    out_of_pocket_cost = total_cost - 3000*0.9

    result = out_of_pocket_cost
    return result

print(solution())