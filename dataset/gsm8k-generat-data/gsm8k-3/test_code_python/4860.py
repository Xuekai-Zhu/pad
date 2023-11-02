def solution():
    """In a factory, there are 3 machines working 23 hours a day. The owner decided to buy a fourth machine, which works only 12 hours a day. One machine can produce 2 kg of material every hour. The factory sells the produced material for $50 per 1 kg. How much can this factory earn in one day?"""
    # Define the number of machines and hours worked
    num_machines = 4
    hours_per_day = 23

    # Calculate the total amount of material produced in one day by all machines
    total_material = (num_machines - 1) * 2 * hours_per_day + 2 * 12

    # Calculate the total revenue earned in one day from selling the material
    total_revenue = total_material * 50

    # Display the total revenue
    result = total_revenue
    return result

print(solution())