def solution():
    
    # Define the cost of one dozen plates
    CUP_COST = 6000

    # Calculate the cost of half a dozen plates
    half_dozen_plates_cost = (20/2) * CUP_COST - 1200

    # Calculate the total cost of buying half a dozen plates
    total_half_dozen_plates_cost = half_dozen_plates_cost * 2

    # Calculate the total cost of buying each cup
    total_cost_per_cup = total_half_dozen_plates_cost / 12

    # Display the total cost of buying each cup
    result = total_cost_per_cup
    return result

print(solution())