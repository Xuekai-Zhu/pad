def solution():
    # Calculate the total cost of Teresa's order
    sandwich_cost = 2 * 7.75  # two fancy ham and cheese sandwiches for $7.75 each
    salami_cost = 4.00
    brie_cost = 3 * salami_cost  # brie is three times the price of the salami
    olives_cost = 10.00 / 4  # 1/4 pound of olives that are $10.00 per pound
    feta_cost = 8.00 / 2  # 1/2 pound of feta cheese that’s $8.00 a pound
    bread_cost = 2.00
    total_cost = sandwich_cost + salami_cost + brie_cost + olives_cost + feta_cost + bread_cost
    result = total_cost
    return result

print(solution())