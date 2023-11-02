def solution():
    num_car_washes = 20
    car_wash_cost = 15
    discount = 0.4  # 60% discount for package purchase

    # Calculate the cost of one car wash after the discount
    discounted_car_wash_cost = car_wash_cost * (1 - discount)

    # Calculate the total cost of the package of 20 car washes
    total_cost = num_car_washes * discounted_car_wash_cost
    result = total_cost
    return result

print(solution())