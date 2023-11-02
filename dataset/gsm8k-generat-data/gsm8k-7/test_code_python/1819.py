def solution():
    num_sandwiches = 2
    sandwich_price = 7.75
    salami_price = 4.0
    brie_price = salami_price * 3
    olives_weight = 0.25
    olives_price_per_lb = 10.0
    feta_weight = 0.5
    feta_price_per_lb = 8.0
    bread_price = 2.0

    # Calculate the total cost of the sandwiches
    total_sandwich_cost = num_sandwiches * sandwich_price

    # Calculate the total cost of the salami
    total_salami_cost = salami_price

    # Calculate the total cost of the brie
    total_brie_cost = brie_price

    # Calculate the total cost of the olives
    total_olives_cost = olives_weight * olives_price_per_lb

    # Calculate the total cost of the feta
    total_feta_cost = feta_weight * feta_price_per_lb

    # Calculate the total cost of the bread
    total_bread_cost = bread_price

    # Calculate the total cost of all items
    total_cost = total_sandwich_cost + total_salami_cost + total_brie_cost + \
                 total_olives_cost + total_feta_cost + total_bread_cost
    result = total_cost
    return result

print(solution())