def solution():
    # Define the number of toy cars and the ratio to toy soldiers
    toy_cars = 20
    toy_soldiers_ratio = 2

    # Calculate the number of toy soldiers
    toy_soldiers = toy_cars * toy_soldiers_ratio

    # Calculate the total number of toys
    total_toys = toy_cars + toy_soldiers
    result = total_toys
    return result

print(solution())