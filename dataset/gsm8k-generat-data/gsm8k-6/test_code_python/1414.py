def solution():
    medicine_cost = 150.00  # cost of 6 month prescription
    cashback = 0.10  # 10% cashback offer
    rebate = 25.00  # mail-in rebate

    # Calculate the total cost of the medicine after cashback and rebate offers
    total_cost = medicine_cost - (medicine_cost * cashback) - rebate
    result = total_cost
    return result

print(solution())