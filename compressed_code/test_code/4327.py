def solution():
    
    melon_price = 3
    profit = 105
    melon_count = 18
    starting_melons = (profit + (melon_count * melon_price)) // melon_price
    result = starting_melons
    return result

print(solution())