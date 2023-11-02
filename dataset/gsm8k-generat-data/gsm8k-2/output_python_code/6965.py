def solution():
    """Darnell pays $12 for unlimited texting and calling on his phone each month. An alternative phone plan would charge $1 per 30 texts and $3 per 20 minutes of calls per month. Darnell sends 60 texts and spends 60 minutes on the phone each month. How many dollars less would he pay on the alternative plan?"""
    unlimited_plan_cost = 12
    alternative_plan_text_cost = (60 // 30) * 1 # calculate number of 30 text message blocks and multiply by $1
    alternative_plan_call_cost = (60 // 20) * 3 # calculate number of 20 minute call blocks and multiply by $3
    alternative_plan_total_cost = alternative_plan_text_cost + alternative_plan_call_cost
    savings = unlimited_plan_cost - alternative_plan_total_cost
    result = savings
    return result

print(solution())