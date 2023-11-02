def solution():
    # Calculate the service fee and total bill
    service_fee = 0.12 * 50 # 12% service fee on $50 worth of food
    total_bill = 50 + service_fee + 5 # $5 tip added to the bill

    result = total_bill
    return result

print(solution())