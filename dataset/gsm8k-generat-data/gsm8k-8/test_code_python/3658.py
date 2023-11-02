def solution():
    # Calculate the total amount paid by the pre-bought ticket passengers
    pre_bought_tickets_total = 20 * 155

    # Calculate the total amount paid by the gate ticket passengers
    gate_tickets_total = 30 * 200

    # Calculate the difference between the two totals
    difference = gate_tickets_total - pre_bought_tickets_total
    result = difference
    return result

print(solution())