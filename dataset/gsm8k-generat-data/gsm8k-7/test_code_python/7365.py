def solution():
    total_money = 42
    num_pizzas = 3
    pizza_cost = 11
    frank_paid = num_pizzas * pizza_cost

    # Calculate how much money Frank gave to Bill
    bill_money = total_money - frank_paid
    bill_total = bill_money + 30

    result = bill_total
    return result

print(solution())