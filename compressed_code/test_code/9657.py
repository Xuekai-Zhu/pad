def solution():
    
    initial_collection = 18
    sold_collection = initial_collection / 2
    sale_price_per_card = 15
    money_earned = sold_collection * sale_price_per_card
    new_postcards_bought = money_earned / 5
    final_collection = initial_collection - sold_collection + new_postcards_bought
    result = final_collection
    return result

print(solution())