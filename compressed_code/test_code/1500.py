def solution():
    
    first_price = 300
    second_price = 350
    first_years = 3
    second_years = 2
    total_months = first_years * 12 + second_years * 12
    total_price = first_price * first_years * 12 + second_price * second_years * 12
    result = total_price
    return result

print(solution())