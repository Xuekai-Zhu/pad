def solution():
    oil_change_price = 20
    num_oil_changes = 5

    repair_price = 30
    num_repairs = 10

    car_wash_price = 5
    num_car_washes = 15

    # Calculate the total earnings from oil changes
    oil_change_earnings = oil_change_price * num_oil_changes

    # Calculate the total earnings from repairs
    repair_earnings = repair_price * num_repairs

    # Calculate the total earnings from car washes
    car_wash_earnings = car_wash_price * num_car_washes

    # Calculate the total earnings from all services
    total_earnings = oil_change_earnings + repair_earnings + car_wash_earnings
    result = total_earnings
    return result

print(solution())