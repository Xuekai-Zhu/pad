def solution():
    """John invests in a bank and gets 10% simple interest. He invests $1000. How much money does he have after 3 years?"""
    principal = 1000
    rate = 0.1
    time = 3
    interest = principal * rate * time
    total_amount = principal + interest
    result = total_amount
    return result

print(solution())