def solution():
    """Teresa orders 2 fancy ham and cheese sandwiches for $7.75 each at a local shop.  While there, she decides to pick up some salami for $4.00, more brie which is three times the price of the salami,  a 1/4 pound of olives that are $10.00 per pound, 1/2 pound of feta cheese that’s $8.00 a pound and another loaf of french bread that is $2.00.  How much does she spend at the local shop?"""
    # Define the prices of each item
    sandwich_price = 7.75
    salami_price = 4.00
    brie_price = 3 * salami_price
    olives_price = 10.00 / 4.00
    feta_price = 8.00 / 2.00
    bread_price = 2.00

    # Calculate the total cost of the sandwiches
    sandwich_cost = 2 * sandwich_price

    # Calculate the total cost of the salami
    salami_cost = salami_price

    # Calculate the total cost of the brie
    brie_cost = brie_price

    # Calculate the total cost of the olives
    olives_cost = olives_price * 0.25

    # Calculate the total cost of the feta
    feta_cost = feta_price * 0.5

    # Calculate the total cost of the bread
    bread_cost = bread_price

    # Calculate the total cost of all the items
    total_cost = sandwich_cost + salami_cost + brie_cost + olives_cost + feta_cost + bread_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())