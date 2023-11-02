def solution():
    # Calculate Liam's total savings
    total_savings = 500 * 12 * 2  

    # Calculate Liam's remaining savings after paying bills
    remaining_savings = total_savings - 3500  

    # Calculate Liam's remaining savings after paying for the Paris trip
    remaining_savings_after_trip = remaining_savings - 7000  

    result = remaining_savings_after_trip
    return result

print(solution())