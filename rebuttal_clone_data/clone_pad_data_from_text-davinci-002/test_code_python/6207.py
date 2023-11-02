def solution():
    treadmill_price = 1350
    treadmill_discount = 30
    plate_price = 50
    plates_bought = 2
    cost_of_treadmill = treadmill_price - (treadmill_price * (treadmill_discount / 100))
    cost_of_plates = plates_bought * plate_price
    total_cost = cost_of_treadmill + cost_of_plates
    result = total_cost
    return result

print(solution())