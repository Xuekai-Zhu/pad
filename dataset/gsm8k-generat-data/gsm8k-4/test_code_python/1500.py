def solution():
    """The Arevalo family went out to dinner. The smoky salmon costs $40, the black burger costs $15, and the chicken katsu costs $25. If the bill includes a 10% service charge and 5% tip, how much change will Mr. Arevalo receive from his $100?"""
    # Define the prices of each meal
    smoky_salmon = 40
    black_burger = 15
    chicken_katsu = 25

    # Calculate the total cost of the meals
    total_cost = smoky_salmon + black_burger + chicken_katsu

    # Calculate the service charge and tip
    service_charge = total_cost * 0.1
    tip = total_cost * 0.05

    # Calculate the total bill
    total_bill = total_cost + service_charge + tip

    # Calculate the change from $100
    change = 100 - total_bill

    result = change
    return result

print(solution())