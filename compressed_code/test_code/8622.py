def solution():
    
    car_income = 20
    dog_income = 40
    total_income = car_income + dog_income
    savings_per_month = total_income / 2
    goal_savings = 150
    months_to_goal = goal_savings / savings_per_month
    result = months_to_goal
    return result

print(solution())