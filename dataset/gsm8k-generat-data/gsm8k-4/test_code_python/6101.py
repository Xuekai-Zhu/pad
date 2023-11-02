def solution():
    """Cary is saving money to buy a new pair of shoes that cost $120. He has already saved $30. He earns $5 for every lawn he mows. If he mows 3 lawns each weekend, how many more weekends will he have to mow lawns before he can afford to buy the shoes?"""
    # Define the cost of the shoes and the amount already saved
    shoe_cost = 120
    amount_saved = 30

    # Calculate the remaining amount to save
    remaining_amount = shoe_cost - amount_saved

    # Calculate the earnings from mowing lawns
    earnings_per_weekend = 5 * 3

    # Calculate the number of weekends needed to save up enough money
    weekends_needed = remaining_amount / earnings_per_weekend

    result = round(weekends_needed)
    return result

print(solution())