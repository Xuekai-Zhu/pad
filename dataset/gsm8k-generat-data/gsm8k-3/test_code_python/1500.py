def solution():
    """The Arevalo family went out to dinner. The smoky salmon costs $40, the black burger costs $15, and the chicken katsu costs $25. If the bill includes a 10% service charge and 5% tip, how much change will Mr. Arevalo receive from his $100?"""
    # Define the prices of each dish
    SALMON_PRICE = 40
    BURGER_PRICE = 15
    KATSU_PRICE = 25

    # Calculate the total cost of the meal before the service charge and tip
    total_cost = SALMON_PRICE + BURGER_PRICE + KATSU_PRICE

    # Calculate the service charge
    service_charge = total_cost * 0.1

    # Calculate the tip
    tip = total_cost * 0.05

    # Calculate the total cost of the meal with the service charge and tip
    total_cost += service_charge + tip

    # Calculate the change from $100
    change = 100 - total_cost

    # Display the change
    result = change
    return result

print(solution())