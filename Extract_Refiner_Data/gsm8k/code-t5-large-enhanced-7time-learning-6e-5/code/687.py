def solution():
    
    # Define the cost of each vaccine and the number of vaccines needed
    VACCINE_COST = 20
    NUM_VACONS = 2

    # Calculate the total cost of the vaccines
    total_cost = VACCINE_COST * NUM_VACONS

    # Calculate the cost of the heartworm check
    heartworm_cost = total_cost * 0.6

    # Calculate the amount left after paying for the heartworm check
    amount_left = 125 - heartworm_cost

    # Display the amount left
    result = amount_left
    return result

print(solution())