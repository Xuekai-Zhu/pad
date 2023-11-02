def solution():
    
    initial_collection = 18
    sold_collection = initial_collection / 2
    price_per_postcard = 15
    money_earned = sold_collection * price_per_postcard
    new_postcards_bought = money_earned / 5
    total_postcards = initial_collection - sold_collection + new_postcards_bought
    result = total_postcards
    return result

print(solution())