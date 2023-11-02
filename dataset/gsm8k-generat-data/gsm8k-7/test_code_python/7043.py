def solution():
    electricity_cost = 60
    gas_cost = 40
    gas_paid = gas_cost * 0.75
    gas_payment = 5
    water_cost = 40
    water_paid = water_cost / 2
    internet_cost = 25
    internet_paid = 4 * 5

    # Calculate the total amount paid for all bills
    total_paid = electricity_cost + gas_paid + gas_payment + water_paid + internet_paid

    # Calculate the total amount still owed for all bills
    total_cost = electricity_cost + gas_cost + water_cost + internet_cost
    amount_due = total_cost - total_paid
    result = amount_due
    return result

print(solution())