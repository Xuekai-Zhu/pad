def solution():
    # Define variables
    total_cars = 5650000
    first_supplier_cars = 1000000
    second_supplier_cars = first_supplier_cars + 500000
    third_supplier_cars = first_supplier_cars + second_supplier_cars
    remaining_cars = total_cars - first_supplier_cars - second_supplier_cars - third_supplier_cars
    
    # Calculate how many cars each of the remaining suppliers get
    fourth_supplier_cars = remaining_cars // 2
    fifth_supplier_cars = remaining_cars // 2
    
    result = (fourth_supplier_cars, fifth_supplier_cars)
    return result

print(solution())