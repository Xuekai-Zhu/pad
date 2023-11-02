def solution():
    laptop_cost = 1000  # The laptop costs $1000
    down_payment = laptop_cost * 0.2 + 20  # Tara needs to make a 20% downpayment plus $20
    balance = laptop_cost - down_payment  # The remaining balance to be paid
    monthly_payment = 65  # Tara can pay $65 per month

    # Calculate the balance after 4 months of payments
    for i in range(4):
        balance -= monthly_payment

    result = balance
    return result

print(solution())