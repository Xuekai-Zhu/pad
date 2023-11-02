def solution():
    # Calculate the total commission earned by Nigella
    commission = 8000 - 3000  # commission is the difference between the total earned and base salary
    total_house_sales = commission / 0.02  # total number of house sales = commission / commission rate
    
    # Calculate the cost of House C
    cost_C = 2 * (total_house_sales - 3) - 110000  # House C cost = 2*(total houses sold - 3) - 110000
    
    # Calculate the cost of House B
    cost_B = 3 * cost_A  # House B cost is three times the cost of House A
    
    # Calculate the cost of House A
    cost_A = (total_house_sales - 3 - cost_C/2 - cost_B/3) / (1 + 2/3)  # using the equation: total_house_sales - 3 - cost_A - cost_B - cost_C = 0
    
    result = cost_A
    return result

print(solution())