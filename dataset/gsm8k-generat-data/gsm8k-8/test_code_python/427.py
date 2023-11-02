def solution():
    starting_amount = 3000
    monthly_savings = 276
    number_of_months = 48
    additional_gift = 7000

    total_savings = starting_amount + (monthly_savings * number_of_months) + additional_gift
    result = total_savings
    return result

print(solution())