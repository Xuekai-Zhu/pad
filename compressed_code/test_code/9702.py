def solution():
    
    total_items = 10  
    bill = 140
    trouser_price = 9
    shirt_price = 5

    total_trouser_cost = total_items * trouser_price
    total_shirt_cost = bill - total_trouser_cost
    missing_shirts = (total_shirt_cost / shirt_price) - 2

    result = missing_shirts

    return result

print(solution())