def solution():
    
    food_cost_per_week = 25
    treats_cost_per_month = 20
    medicine_cost_per_month = 100
    weeks_per_month = 4
    total_food_cost_per_month = food_cost_per_week * weeks_per_month
    total_treats_cost_per_month = treats_cost_per_month * weeks_per_month
    total_medicine_cost_per_month = medicine_cost_per_month * weeks_per_month
    total_cost_per_year = total_food_cost_per_month + total_treats_cost_per_month + total_medicine_cost_per_month
    result = total_cost_per_year
    return result

print(solution())