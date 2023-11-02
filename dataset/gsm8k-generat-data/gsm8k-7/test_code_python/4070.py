def solution():
    daily_ingredient_cost = 10
    weekly_ingredient_cost = daily_ingredient_cost * 7
    
    french_fries_price = 12
    poutine_price = 8
    
    num_french_fries = 7 # assuming Lucius makes one portion of French Fries every day
    num_poutine = 7 # assuming Lucius makes one portion of Poutine every day
    
    total_sales = (num_french_fries * french_fries_price) + (num_poutine * poutine_price)
    
    weekly_income = total_sales - weekly_ingredient_cost
    
    tax = 0.1 # ten percent tax
    
    net_income = weekly_income - (weekly_income * tax)
    
    result = net_income
    return result

print(solution())