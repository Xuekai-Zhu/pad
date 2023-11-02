def solution():
    salary = 150000
    savings_rate = 0.1
    downpayment_percentage = 0.2
    house_cost = 450000
    downpayment_amount = house_cost * downpayment_percentage
    savings_per_year = salary * savings_rate
    years_to_save = downpayment_amount / savings_per_year
    result = years_to_save
    return result

print(solution())