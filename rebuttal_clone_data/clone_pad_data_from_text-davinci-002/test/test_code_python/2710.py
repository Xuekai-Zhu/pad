def solution():
    initial_rental_cost = 150
    gallons_of_gas = 8
    gas_cost_per_gallon = 3.50
    drive_distance = 320
    gas_cost = gallons_of_gas * gas_cost_per_gallon
    final_expense_per_mile = 0.50
    final_expense = final_expense_per_mile * drive_distance
    total_cost = initial_rental_cost + gas_cost + final_expense
    result = total_cost
    
    return result

print(solution())