def solution():
    grocery_store = 10
    mall = 6
    pet_store = 5
    home = 9
    gas_mileage = 15
    gas_price = 3.50
    total_miles = grocery_store + mall + pet_store + home
    total_gallons = total_miles / gas_mileage
    total_cost = total_gallons * gas_price
    result = total_cost
    
    return result

print(solution())