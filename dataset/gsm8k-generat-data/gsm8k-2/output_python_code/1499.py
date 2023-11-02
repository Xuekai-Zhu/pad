def solution():
    """The Arevalo family went out to dinner. The smoky salmon costs $40, the black burger costs $15, and the chicken katsu costs $25. If the bill includes a 10% service charge and 5% tip, how much change will Mr. Arevalo receive from his $100?"""
    salmon_cost = 40
    burger_cost = 15
    katsu_cost = 25
    subtotal = salmon_cost + burger_cost + katsu_cost
    service_charge = 0.1 * subtotal
    tip = 0.05 * subtotal
    total_cost = subtotal + service_charge + tip
    change = 100 - total_cost
    result = change
    return result

print(solution())