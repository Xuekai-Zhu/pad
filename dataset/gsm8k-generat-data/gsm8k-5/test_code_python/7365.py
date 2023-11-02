def solution():
    total_money = 42  # Frank and Bill have a total of $42
    num_pizzas = 3  # They bought 3 pizzas
    cost_per_pizza = 11  # Each pizza costs $11

    # Calculate how much Frank paid for the pizzas
    frank_paid = num_pizzas * cost_per_pizza

    # Calculate how much money Frank has left after buying the pizzas
    frank_money = total_money - frank_paid

    # Calculate how much money Bill has now
    bill_money = frank_money + 30

    result = bill_money
    return result

print(solution())