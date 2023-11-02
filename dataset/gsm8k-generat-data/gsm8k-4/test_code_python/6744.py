def solution():
    """Genevieve picked some cherries from the supermarket shelves that cost $8 per kilogram. When Genevieve reached the checkout counter, she realized she was $400 short of the total price and her friend Clarice chipped in. If Genevieve had $1600 on her, how many kilograms of cherries did she buy?"""
    # Define the cost per kilogram and the amount Genevieve had
    COST_PER_KG = 8
    GENEVIEVE_AMOUNT = 1600

    # Calculate the total cost of the cherries
    total_cost = GENEVIEVE_AMOUNT + 400

    # Calculate the weight of the cherries Genevieve bought
    cherries_weight = total_cost / COST_PER_KG

    result = cherries_weight
    return result

print(solution())