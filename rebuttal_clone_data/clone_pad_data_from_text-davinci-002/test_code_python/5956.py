def solution():
    total_ kilometers = 150
    gas_price = 0.90
    kilometers_per_liter = 15
    car_rental_option1 = 50
    car_rental_option2 = 90
    liters_of_gas = total_kilometers / kilometers_per_liter
    cost_of_gas = liters_of_gas * gas_price
    total_cost_option1 = car_rental_option1 + cost_of_gas
    total_cost_option2 = car_rental_option2
    savings = total_cost_option2 - total_cost_option1
    result = savings
    return result

print(solution())