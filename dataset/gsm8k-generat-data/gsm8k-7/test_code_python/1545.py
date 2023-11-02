def solution():
    num_toys = 3
    toy_price = 10

    num_basketball_cards = 2
    basketball_cards_price = 5

    num_shirts = 5
    shirt_price = 6

    # Calculate the total cost of all toys
    total_toys_cost = num_toys * toy_price

    # Calculate the total cost of all basketball cards
    total_basketball_cards_cost = num_basketball_cards * basketball_cards_price

    # Calculate the total cost of all shirts
    total_shirts_cost = num_shirts * shirt_price

    # Calculate the total cost of all presents
    total_cost = total_toys_cost + total_basketball_cards_cost + total_shirts_cost
    result = total_cost
    return result

print(solution())