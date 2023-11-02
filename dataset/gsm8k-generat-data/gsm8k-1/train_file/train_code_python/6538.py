def solution():
    """American carmakers produce 5 650 000 cars each year. Then they distribute it to 5 car suppliers. The first supplier receives 1 000 000 cars each. The second supplier receives 500 000 cars more while the third car supplier receives the same number as the first and second suppliers combined. The fourth and the fifth supplier receive an equal number of cars. How many cars do the fourth and fourth suppliers each receive?"""
    total_cars = 5650000
    first_supplier_cars = 1000000
    second_supplier_cars = first_supplier_cars + 500000
    third_supplier_cars = first_supplier_cars + second_supplier_cars
    remaining_cars = total_cars - first_supplier_cars - second_supplier_cars - third_supplier_cars
    fourth_supplier_cars = remaining_cars / 2
    fifth_supplier_cars = fourth_supplier_cars
    result = (fourth_supplier_cars, fifth_supplier_cars)
    return result

print(solution())