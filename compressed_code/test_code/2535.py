def solution():
    
    weekly_latte_cost = 4 * 5
    weekly_iced_coffee_cost = 2 * 3
    yearly_latte_cost = weekly_latte_cost * 52
    yearly_iced_coffee_cost = weekly_iced_coffee_cost * 52
    total_spending = yearly_latte_cost + yearly_iced_coffee_cost
    savings = total_spending * 0.25
    result = savings
    return result

print(solution())