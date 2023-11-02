def solution():
    # Calculate the total cost of the accident
    total_cost = 40000 + 70000  

    # Calculate the amount Carl's insurance company will pay
    insurance_payment = 0.8 * total_cost  

    # Calculate the amount Carl personally owes
    remaining_cost = total_cost - insurance_payment  
    result = remaining_cost
    return result

print(solution())