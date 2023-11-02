def solution():
    """Genevieve picked some cherries from the supermarket shelves that cost $8 per kilogram. When Genevieve reached the checkout counter, she realized she was $400 short of the total price and her friend Clarice chipped in. If Genevieve had $1600 on her, how many kilograms of cherries did she buy?"""
    # Define the cost per kilogram of cherries
    CHERRY_PRICE = 8

    # Define the amount of money Genevieve had and was short of
    GENEVIEVE_MONEY = 1600
    SHORTAGE = 400

    # Calculate the total cost of the cherries
    total_cost = GENEVIEVE_MONEY + SHORTAGE

    # Calculate the weight of the cherries Genevieve bought
    weight = total_cost / CHERRY_PRICE

    # Display the weight of the cherries
    result = weight
    return result

print(solution())