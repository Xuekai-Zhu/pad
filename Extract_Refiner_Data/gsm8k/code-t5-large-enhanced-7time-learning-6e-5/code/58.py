def solution():
    
    # Define the initial annual pension and the annual pension-value ratio
    annual_pension = 50000
    annual_pension_ratio = 0.05

    # Calculate the annual pension value after 20 years
    annual_pension_value = annual_pension * annual_pension_ratio

    # Calculate the annual pension value after 20 years
    annual_pension_value *= (1 - annual_pension_ratio)

    # Calculate the annual pension value after 30 years
    annual_pension_value *= (1 - annual_pension_ratio)

    # Display the annual pension value
    result = annual_pension_value
    return result

print(solution())