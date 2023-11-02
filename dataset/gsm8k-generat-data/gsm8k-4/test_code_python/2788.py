def solution():
    """Dr. Jones earns $6,000 a month. His house rental is $640 each month; his monthly food expense is $380; his electric and water bill costs 1/4 of what he makes, and his insurances cost 1/5 of what he makes. How much money does he have left after paying those four bills?"""
    # Define Dr. Jones' monthly earnings
    earnings = 6000

    # Define Dr. Jones' monthly expenses
    house_rental = 640
    food_expense = 380
    electric_water_bill = earnings * 1/4
    insurance_cost = earnings * 1/5

    # Calculate the total monthly expenses
    total_expenses = house_rental + food_expense + electric_water_bill + insurance_cost

    # Calculate Dr. Jones' left over money after paying the bills
    left_over = earnings - total_expenses

    result = left_over
    return result

print(solution())