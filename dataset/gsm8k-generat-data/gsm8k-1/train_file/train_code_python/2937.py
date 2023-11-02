def solution():
    """Mike is saving up to buy a house. He puts away 10% of his $150,000 a year salary. He needs to save up 20% of the cost of a $450,000 house for a downpayment. How long will it take?"""
    annual_salary = 150000
    savings_rate = 0.1
    downpayment_percent = 0.2
    house_cost = 450000
    downpayment_amount = house_cost * downpayment_percent
    yearly_savings = annual_salary * savings_rate
    years_to_save = downpayment_amount / yearly_savings
    result = years_to_save
    
    return result

print(solution())