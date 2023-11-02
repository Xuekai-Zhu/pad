def solution():
    
    unlimited_plan_cost = 12
    alternative_plan_text_cost = (60 // 30) * 1 
    alternative_plan_call_cost = (60 // 20) * 3 
    alternative_plan_total_cost = alternative_plan_text_cost + alternative_plan_call_cost
    savings = unlimited_plan_cost - alternative_plan_total_cost
    result = savings
    return result

print(solution())