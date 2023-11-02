def solution():
    # Calculate the total number of cars received by the first three suppliers
    first_supplier_cars = 1000000
    second_supplier_cars = first_supplier_cars + 500000
    third_supplier_cars = first_supplier_cars + second_supplier_cars

    # Calculate the total number of cars received by the first three suppliers
    total_first_third_suppliers = first_supplier_cars + second_supplier_cars + third_supplier_cars

    # Calculate the number of cars received by the fourth and fifth suppliers
    fourth_supplier_cars = (5650000 - total_first_third_suppliers) / 2
    fifth_supplier_cars = fourth_supplier_cars

    result = (fourth_supplier_cars, fifth_supplier_cars)
    return result

print(solution())