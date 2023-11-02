def solution():
    maize_per_month = 1  # 1 tonne per month
    num_years = 2
    total_maize = 0
    
    # Calculate the total maize stored over 2 years
    for i in range(num_years * 12):
        total_maize += maize_per_month
    
    # Subtract stolen and donated maize
    total_maize -= 5
    total_maize += 8
    
    result = total_maize
    return result

print(solution())