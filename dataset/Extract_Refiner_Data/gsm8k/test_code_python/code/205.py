def solution():
    
    # Define the cost of each plate
    PLATE_COST = 6000

    # Calculate the total cost of buying half a dozen cups
    half_dozen_cost = PLATE_COST / 2

    # Calculate the cost of buying 20 dozen cups
    dozen_cost = half_dozen_cost - 1200

    # Calculate the total cost of buying 20 dozen cups
    total_half_dozen_cost = dozen_cost * 12

    # Calculate the total cost of buying 20 dozen cups
    total_cost = total_half_dozen_cost * 12

    # Display the total cost
    result = total_cost
    return result

print(solution())