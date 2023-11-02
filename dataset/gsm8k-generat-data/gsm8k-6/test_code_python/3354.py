def solution():
    # Calculate the amount Mr. Lalande has to pay in total
    total_payment = 18000 - 3000  # Mr. Lalande paid 3000 euros initially
    monthly_payment = total_payment / 6  # divide the remaining amount by 6 monthly installments
    result = monthly_payment
    return result

print(solution())