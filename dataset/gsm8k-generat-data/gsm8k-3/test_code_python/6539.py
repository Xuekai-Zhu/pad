def solution():
    """American carmakers produce 5 650 000 cars each year. Then they distribute it to 5 car suppliers. The first supplier receives 1 000 000 cars each. The second supplier receives 500 000 cars more while the third car supplier receives the same number as the first and second suppliers combined. The fourth and the fifth supplier receive an equal number of cars. How many cars do the fourth and fourth suppliers each receive?"""
    # Define the total number of cars produced
    total_cars = 5650000

    # Define the number of cars received by the first supplier
    supplier_1_cars = 1000000

    # Define the number of cars received by the second supplier, which is 500,000 more than the first
    supplier_2_cars = supplier_1_cars + 500000

    # Define the number of cars received by the third supplier, which is the sum of the first and second
    supplier_3_cars = supplier_1_cars + supplier_2_cars

    # Define the number of remaining cars after the first three suppliers
    remaining_cars = total_cars - supplier_1_cars - supplier_2_cars - supplier_3_cars

    # Divide the remaining cars equally between the fourth and fifth suppliers
    supplier_4_cars = remaining_cars/2
    supplier_5_cars = remaining_cars/2

    # Display the number of cars received by the fourth and fifth suppliers
    result = (supplier_4_cars, supplier_5_cars)
    return result

print(solution())