def solution():
    initial_funds = 2000
    supplier_payment = 600
    debtor_payment = 800
    equipment_maintenance_cost = 1200

    # Calculate the total amount of money spent
    total_spent = supplier_payment + equipment_maintenance_cost

    # Calculate the total amount of money received
    total_received = debtor_payment

    # Calculate the remaining funds
    remaining_funds = initial_funds + total_received - total_spent
    result = remaining_funds
    return result

print(solution())