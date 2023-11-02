def solution():
    # Calculate the total cost of the pizzas
    pizza_cost = 11 * 3

    # Calculate how much money Frank gave to Bill
    frank_to_bill = 42 - pizza_cost

    # Add Frank's remaining money to what he gave to Bill
    bill_money = frank_to_bill + 30
    result = bill_money
    return result

print(solution())