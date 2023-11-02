def solution():
    """Dr. Jones earns $6,000 a month. His house rental is $640 each month; his monthly food expense is $380; his electric and water bill costs 1/4 of what he makes, and his insurances cost 1/5 of what he makes. How much money does he have left after paying those four bills?"""
    # Define Dr. Jones' monthly expenses
    HOUSE_RENTAL = 640
    FOOD_EXPENSE = 380
    ELECTRIC_WATER_BILL_PERCENTAGE = 0.25
    INSURANCE_PERCENTAGE = 0.2

    # Calculate Dr. Jones' monthly electric and water bill cost
    electric_water_bill_cost = ELECTRIC_WATER_BILL_PERCENTAGE * 6000

    # Calculate Dr. Jones' monthly insurance cost
    insurance_cost = INSURANCE_PERCENTAGE * 6000

    # Calculate Dr. Jones' total monthly expenses
    total_expenses = HOUSE_RENTAL + FOOD_EXPENSE + electric_water_bill_cost + insurance_cost

    # Calculate Dr. Jones' monthly income after expenses
    income_after_expenses = 6000 - total_expenses

    # Display Dr. Jones' monthly income after expenses
    result = income_after_expenses
    return result

print(solution())