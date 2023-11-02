def solution():
    total_mileage = 450  # Arnold drives a total of 450 miles per month
    mileage_per_car = total_mileage / 3  # Arnold splits the mileage equally amongst his cars

    # Calculate the total gallons of gas needed for each car
    gallons_car1 = mileage_per_car / 50
    gallons_car2 = mileage_per_car / 10
    gallons_car3 = mileage_per_car / 15

    # Calculate the total cost for gas
    total_cost = (gallons_car1 + gallons_car2 + gallons_car3) * 2

    result = total_cost
    return result

print(solution())