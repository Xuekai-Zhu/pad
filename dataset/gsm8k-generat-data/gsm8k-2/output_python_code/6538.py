def solution():
    """American carmakers produce 5 650 000 cars each year. Then they distribute it to 5 car suppliers. The first supplier receives 1 000 000 cars each. The second supplier receives 500 000 cars more while the third car supplier receives the same number as the first and second suppliers combined. The fourth and the fifth supplier receive an equal number of cars. How many cars do the fourth and fourth suppliers each receive?"""
    total_cars = 5650000
    first_supplier = 1000000
    second_supplier = first_supplier + 500000
    third_supplier = first_supplier + second_supplier
    remaining_cars = total_cars - (first_supplier + second_supplier + third_supplier)
    fourth_supplier = fifth_supplier = remaining_cars / 2
    result = (fourth_supplier, fifth_supplier)
    return result

print(solution())