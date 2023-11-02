def solution():
    # Define the prices at each salon
    gustran_prices = [45, 22, 30]
    barbara_prices = [30, 28, 40]
    fancy_prices = [34, 30, 20]

    # Calculate the total cost at each salon
    gustran_cost = sum(gustran_prices)
    barbara_cost = sum(barbara_prices)
    fancy_cost = sum(fancy_prices)

    # Find the cheapest salon
    cheapest_cost = min(gustran_cost, barbara_cost, fancy_cost)

    return cheapest_cost

print(solution())