def solution():
    old_spending_percentage = 0.4
    new_spending_percentage = 0.25
    increase = 600

    # Let's assume her old monthly income is x
    # Calculate the amount she used to spend on rent and utilities
    old_rent_utilities = old_spending_percentage * x

    # Calculate her new monthly income
    new_monthly_income = x + increase

    # Calculate the new amount she spends on rent and utilities
    new_rent_utilities = new_spending_percentage * new_monthly_income

    # Since the amount spent on rent and utilities remains the same, we can equate the two
    # equations: old_rent_utilities = new_rent_utilities
    # Substitute the values and solve for x
    x = new_rent_utilities / old_spending_percentage
    result = x
    return result

print(solution())