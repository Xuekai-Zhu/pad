def solution():
    monthly_cost = 10  # The monthly subscription fee is $10
    annual_cost = monthly_cost * 12  # The total annual cost without discount is $120
    discount = 0.20  # The discount for an annual subscription is 20%

    # Calculate the final cost with the discount
    final_cost = annual_cost * (1 - discount)
    result = final_cost
    return result

print(solution())