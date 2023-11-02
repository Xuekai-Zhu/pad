def solution():
    latte_cost = 4
    latte_days = 5
    iced_cost = 2
    iced_days = 3
    days_in_week = 7
    weeks_in_year = 52
    total_latte_cost = latte_cost * latte_days * weeks_in_year
    total_iced_cost = iced_cost * iced_days * weeks_in_year
    total_yearly_cost = total_latte_cost + total_iced_cost
    percent_decrease = 25
    decrease_amount = total_yearly_cost * (percent_decrease / 100)
    total_yearly_spending_after_decrease = total_yearly_cost - decrease_amount
    result = total_yearly_spending_after_decrease
    
    return result

print(solution())