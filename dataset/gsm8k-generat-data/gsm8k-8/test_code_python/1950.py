def solution():
    # Define the number of chocolate bars and bags of chips purchased
    num_chocolate_bars = 5
    num_chips_bags = 2

    # Define the total cost of the chocolate bars
    total_chocolate_bars_cost = num_chocolate_bars * 2

    # Calculate the total cost of the purchase
    total_purchase_cost = total_chocolate_bars_cost + (x * num_chips_bags)

    # Calculate the amount paid by Frank
    franks_payment = total_purchase_cost - 4

    # Calculate the cost of one bag of chips
    x = (franks_payment - total_chocolate_bars_cost) / num_chips_bags

    result = x
    return result

print(solution())