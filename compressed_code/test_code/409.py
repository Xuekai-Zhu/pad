def solution():
    
    total_budget = 240
    food_budget_ratio = 0.6
    phone_bill_ratio = 0.1
    house_rental_budget = total_budget / (food_budget_ratio + 1)
    food_budget = food_budget_ratio * house_rental_budget
    phone_bill_budget = phone_bill_ratio * food_budget
    total_expenses = house_rental_budget + food_budget + phone_bill_budget
    result = total_expenses
    return result

print(solution())