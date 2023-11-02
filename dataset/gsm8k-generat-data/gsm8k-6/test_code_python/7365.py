def solution():
    # Calculate the amount of money Frank paid for the pizzas
    pizza_cost = 11 * 3
    frank_paid = pizza_cost

    # Calculate the amount of money Frank gave to Bill
    bill_received = 42 - frank_paid

    # Calculate the total amount of money Bill has now
    bill_total = bill_received + 30
    result = bill_total
    return result

print(solution())