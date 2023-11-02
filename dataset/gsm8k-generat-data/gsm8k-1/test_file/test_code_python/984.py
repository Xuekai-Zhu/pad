def solution():
    """Jessica makes $2,000.00 a month. She sets 25% of her paycheck aside to put towards fancy shoes. Each pair of shoes she buys costs $1,000.00. How many shoes can she buy in a year?"""
    monthly_income = 2000
    savings_percentage = 0.25
    shoes_cost = 1000
    yearly_savings = monthly_income * savings_percentage * 12
    shoes_per_year = yearly_savings // shoes_cost
    result = shoes_per_year
    return result

print(solution())