def solution():
    """Sally is saving up for a trip to Sea World. She already has $28 saved. It costs her $10 to park, $55 to get into the park and $25 for a meal pass. Sea World is 165 miles away and her car gets 30 miles per gallon of gas. If gas costs $3 a gallon, how much more will she have to save up?"""
    initial_savings = 28
    parking_cost = 10
    park_ticket_cost = 55
    meal_pass_cost = 25
    total_expenses = parking_cost + park_ticket_cost + meal_pass_cost
    
    miles = 165
    miles_per_gallon = 30
    gas_price = 3
    gallons_needed = miles / miles_per_gallon
    gas_cost = gallons_needed * gas_price
    
    total_cost = initial_savings + total_expenses + gas_cost
    amount_to_save = total_cost - initial_savings
    
    result = amount_to_save
    return result

print(solution())