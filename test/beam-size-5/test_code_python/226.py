def solution():
    num_cars = 12
    car_price = 20000
    tax_rate = 0.1
    registration_rate = 1000

    # Calculate the total cost of all cars before tax
    total_cost_before_tax = num_cars * car_price

    # Calculate the amount of tax
    tax = total_cost_before_tax * tax_rate

    # Calculate the total cost of all registration
    total_registration_cost = num_cars * registration_rate

    # Calculate the total cost of everything
    total_cost = total_cost_before_tax + total_registration_cost
    result = total_cost
    return result

print(solution())