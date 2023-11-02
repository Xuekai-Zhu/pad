def solution():
    """Darnell pays $12 for unlimited texting and calling on his phone each month. An alternative phone plan would charge $1 per 30 texts and $3 per 20 minutes of calls per month. Darnell sends 60 texts and spends 60 minutes on the phone each month. How many dollars less would he pay on the alternative plan?"""
    unlimited_cost = 12
    texts = 60
    minutes = 60
    text_cost = 1/30
    minute_cost = 3/20
    alternative_cost = texts * text_cost + minutes * minute_cost
    savings = unlimited_cost - alternative_cost
    result = savings
    
    return result

print(solution())