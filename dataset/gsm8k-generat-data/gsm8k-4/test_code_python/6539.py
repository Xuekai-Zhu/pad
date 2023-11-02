def solution():
    """American carmakers produce 5 650 000 cars each year. Then they distribute it to 5 car suppliers. The first supplier receives 1 000 000 cars each. The second supplier receives 500 000 cars more while the third car supplier receives the same number as the first and second suppliers combined. The fourth and the fifth supplier receive an equal number of cars. How many cars do the fourth and fourth suppliers each receive?"""
    # Define the total number of cars produced and distributed
    total_cars = 5650000

    # Define the number of cars received by the first supplier
    supplier_1_cars = 1000000

    # Define the number of cars received by the second supplier
    supplier_2_cars = supplier_1_cars + 500000

    # Define the number of cars received by the third supplier
    supplier_3_cars = supplier_1_cars + supplier_2_cars

    # Calculate the number of cars received by the fourth and fifth suppliers
    supplier_4_5_cars = (total_cars - supplier_1_cars - supplier_2_cars - supplier_3_cars) / 2

    # Return the results
    result = (supplier_4_5_cars, supplier_4_5_cars)
    return result

print(solution())