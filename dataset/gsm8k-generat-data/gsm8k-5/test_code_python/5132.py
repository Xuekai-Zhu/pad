def solution():
    oil_change_cost = 20  # Cid charges $20 for an oil change
    oil_change_cars = 5  # Cid changed the oil of 5 cars

    repair_cost = 30  # Cid charges $30 for a repair
    repair_cars = 10  # Cid repaired 10 cars

    car_wash_cost = 5  # Cid charges $5 for a car wash
    car_wash_cars = 15  # Cid washed 15 cars

    # Calculate the total money earned
    total_earnings = (oil_change_cost * oil_change_cars) + (repair_cost * repair_cars) + (car_wash_cost * car_wash_cars)
    result = total_earnings
    return result

print(solution())