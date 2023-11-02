def solution():
    num_sheep = 200
    shearer_payment = 2000
    wool_per_sheep = 10
    wool_price_per_pound = 20

    # Calculate the total amount of wool produced
    total_wool = num_sheep * wool_per_sheep

    # Calculate the total revenue from selling the wool
    total_revenue = total_wool * wool_price_per_pound

    # Calculate the profit by subtracting the shearer payment from the total revenue
    profit = total_revenue - shearer_payment
    result = profit
    return result

print(solution())