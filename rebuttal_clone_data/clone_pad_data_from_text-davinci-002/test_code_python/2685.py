def solution():
    daily_rate = 125
    pet_fee = 100
    service_fee = 20
    security_deposit = 50
    total_bill = (daily_rate + pet_fee) * (1 + service_fee / 100)
    result = total_bill * security_deposit / 100
    return result

print(solution())