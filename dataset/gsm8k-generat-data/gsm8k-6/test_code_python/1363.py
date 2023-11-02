def solution():
    # Calculate the total cost of making the cupcakes
    cost = 0.75 * (2*12 + 2*12 + 2*12)  # Prudence made a total of 6 dozen cupcakes

    # Calculate the number of cupcakes remaining after throwing out burnt cupcakes and eating some
    remaining_cupcakes = (2*12 + 2*12 + 2*12) - (2*12 + 5 + 4)

    # Calculate the total revenue from selling the remaining cupcakes
    revenue = remaining_cupcakes * 2

    # Calculate the net profit
    net_profit = revenue - cost
    result = net_profit
    return result

print(solution())