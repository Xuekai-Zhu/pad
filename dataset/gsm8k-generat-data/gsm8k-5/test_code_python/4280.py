def solution():
    rent_percentage = 7  # Zilla spent 7% of her monthly earnings on rent
    rent_amount = 133  # Zilla spent $133 on her rent
    total_percentage = 100  # The total percentage of Zilla's monthly earnings is 100%
    expenses_percentage = rent_percentage / 2  # Zilla spent half of her remaining earnings on other monthly expenses
    savings_percentage = total_percentage - rent_percentage - expenses_percentage  # Zilla puts the rest in her savings account

    # Calculate Zilla's total monthly earnings
    total_earnings = rent_amount / (rent_percentage / 100)

    # Calculate the amount Zilla deposits into her savings account
    savings_amount = total_earnings * (savings_percentage / 100)
    result = savings_amount
    return result

print(solution())