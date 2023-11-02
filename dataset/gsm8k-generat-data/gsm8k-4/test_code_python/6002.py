def solution():
    """Kathryn moved to a new city for the new job she had landed two weeks ago. Her rent was $1200, 1/2 of what she spent on food and travel expenses in a month. Luckily, she found a new friend Shelby, who moved in with her to share the rent. If her salary was $5000 per month, how much money remained after her expenses?"""
    # Define the monthly rent
    monthly_rent = 1200

    # Calculate the monthly budget for food and travel expenses
    food_travel_budget = monthly_rent * 2

    # Calculate Kathryn's monthly expenses
    total_expenses = monthly_rent + food_travel_budget

    # Calculate the amount Shelby contributes to the rent
    shelby_rent_contribution = monthly_rent / 2

    # Calculate Kathryn's net income after subtracting expenses and rent contribution
    net_income = 5000 - total_expenses - shelby_rent_contribution

    # Return the result
    result = net_income
    return result

print(solution())