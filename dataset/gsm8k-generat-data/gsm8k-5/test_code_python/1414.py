def solution():
    medicine_cost = 150.00  # Stacy paid $150.00 for the 6-month prescription
    cashback = 0.10  # Stacy gets 10% cashback on her purchase
    rebate = 25.00  # Stacy has a $25.00 mail-in rebate for the 6-month prescription

    # Calculate the total amount of cashback Stacy will receive
    total_cashback = medicine_cost * cashback

    # Calculate the total cost of the medicine after cashback and rebate offers
    total_cost = medicine_cost - total_cashback - rebate
    result = total_cost
    return result

print(solution())