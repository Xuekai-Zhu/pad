def solution():
    num_machines = 4
    machine_hours = [23, 23, 23, 12]
    production_rate = 2  # kg per hour
    selling_price = 50  # dollars per kg

    # Calculate the total production of all machines in one day
    total_production = sum(machine_hours) * num_machines * production_rate

    # Calculate the total revenue generated from selling the produced material
    total_revenue = total_production * selling_price

    result = total_revenue
    return result

print(solution())