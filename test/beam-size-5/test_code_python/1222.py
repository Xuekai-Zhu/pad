def solution():
    
    # Define the initial cost of the manicure and pedicure
    manicure_cost = 35
    pedicure_cost = 40

    # Calculate the discounted cost of the manicure and pedicure
    manicure_discounted_cost = manicure_cost - (manicure_cost * 0.8)
    pedicure_discounted_cost = pedicure_cost - (pedicure_cost * 0.8)

    # Calculate the total cost of both fingers
    total_cost = manicure_discounted_cost + pedicure_discounted_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())