def solution():
    monthly_income = 6000
    house_rental = 640
    food_expense = 380
    electric_water_bill = monthly_income / 4
    insurance_cost = monthly_income / 5

    # Calculate the total amount of bills
    total_bills = house_rental + food_expense + electric_water_bill + insurance_cost

    # Calculate the amount of money Dr. Jones has left
    money_left = monthly_income - total_bills
    result = money_left
    return result

print(solution())