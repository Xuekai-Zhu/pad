def solution():
    """Teresa orders 2 fancy ham and cheese sandwiches for $7.75 each at a local shop. While there, she decides to pick up some salami for $4.00, more brie which is three times the price of the salami, a 1/4 pound of olives that are $10.00 per pound, 1/2 pound of feta cheese that’s $8.00 a pound and another loaf of french bread that is $2.00. How much does she spend at the local shop?"""
    # Calculate the cost of the sandwiches
    sandwich_cost = 2 * 7.75

    # Calculate the cost of the salami
    salami_cost = 4.00

    # Calculate the cost of the brie (3 times the price of the salami)
    brie_cost = 3 * salami_cost

    # Calculate the cost of the olives (1/4 pound at $10.00 per pound)
    olives_cost = 0.25 * 10.00

    # Calculate the cost of the feta cheese (1/2 pound at $8.00 per pound)
    feta_cost = 0.5 * 8.00

    # Calculate the cost of the french bread
    bread_cost = 2.00

    # Calculate the total cost of the items
    total_cost = sandwich_cost + salami_cost + brie_cost + olives_cost + feta_cost + bread_cost

    result = total_cost
    return result

print(solution())