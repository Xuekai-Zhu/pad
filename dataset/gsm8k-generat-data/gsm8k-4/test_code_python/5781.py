def solution():
    """Candice buys all the bread she and her family needs for the week from a local bakery. She needs 2 loaves of white bread for sandwiches that cost $3.50 each. She also needs a baguette that costs $1.50 and 2 loaves of sourdough bread that cost $4.50 each. She also treats herself to a $2.00 almond croissant each visit. How much does Candice spend at the bakery over 4 weeks?"""
    # Define the prices of the various items
    white_bread_price = 3.5
    baguette_price = 1.5
    sourdough_bread_price = 4.5
    croissant_price = 2.0

    # Calculate the total cost of one visit to the bakery
    total_cost_per_visit = (2 * white_bread_price) + baguette_price + (2 * sourdough_bread_price) + croissant_price

    # Calculate the total cost of 4 visits to the bakery
    total_cost = total_cost_per_visit * 4

    result = total_cost
    return result

print(solution())