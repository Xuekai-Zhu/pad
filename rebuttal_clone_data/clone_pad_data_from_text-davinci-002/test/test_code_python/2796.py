def solution():
    initial_collection = 18
    postcards_sold = initial_collection / 2
    money_earned = postcards_sold * 15
    postcards_bought = money_earned / 5
    final_collection = initial_collection - postcards_sold + postcards_bought
    result = final_collection
    return result

print(solution())