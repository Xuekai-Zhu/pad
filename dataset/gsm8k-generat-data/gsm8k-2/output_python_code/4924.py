def solution():
    """Bernie has a collection of 18 unique postcards. He decided to sell half his collection for $15 per postcard.
    After he has successfully sold his postcards he decided to spend all the earned money to buy new postcards for $5 each.
    How many postcards does Bernie have after all his transactions?"""
    initial_collection = 18
    sold_collection = initial_collection / 2
    price_per_postcard = 15
    money_earned = sold_collection * price_per_postcard
    new_postcards_bought = money_earned / 5
    total_postcards = initial_collection - sold_collection + new_postcards_bought
    result = total_postcards
    return result

print(solution())