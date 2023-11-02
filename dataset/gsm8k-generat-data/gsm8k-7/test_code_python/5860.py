def solution():
    repair_fee = 10
    corner_light_price = 2 * repair_fee
    brake_disk_price = 3 * corner_light_price
    total_spent = repair_fee + corner_light_price + (2 * brake_disk_price)
    total_savings = total_spent + 480
    initial_savings = total_savings - repair_fee
    result = initial_savings
    return result

print(solution())